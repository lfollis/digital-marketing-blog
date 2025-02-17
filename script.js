const outputDiv = document.getElementById('output');
const userInput = document.getElementById('user-input');

function printToOutput(text) {
    outputDiv.innerHTML += text.replace(/\n/g, "<br>"); // Use <br> for newlines in HTML
    outputDiv.scrollTop = outputDiv.scrollHeight;
}

let quizState = null;
let pyodide = null; // Declare pyodide at a higher scope

async function loadPyodide() {
    pyodide = await pyodide.loadPyodide({ indexURL : "https://cdn.jsdelivr.net/pyodide/v0.22.1/full/" });
    await pyodide.loadPackage(['micropip']);
    await pyodide.runPythonAsync('import io; import sys; sys.stdout = io.StringIO()');
}


async function runPythonQuiz() {
    if (!pyodide) {
        await loadPyodide(); // Ensure Pyodide is loaded
    }

    const input = userInput.value;
    userInput.value = '';

    if (quizState === null) {
        try {
            const pythonCode = await fetch('what-to-do-quiz.py').then(r => r.text()); // Fetch Python code
            await pyodide.runPythonAsync(pythonCode); // Load the Python code into Pyodide

            quizState = await pyodide.runPythonAsync(`
                import io
                import sys

                old_stdout = sys.stdout
                sys.stdout = io.StringIO()

                tourist_attraction_quiz()

                captured_output = sys.stdout.getvalue()
                sys.stdout = old_stdout
                js.printToOutput(captured_output)

                return {
                    "fitness_quiz": fitness_quiz,
                    "outdoor_quiz": outdoor_quiz,
                    "foodie_quiz": foodie_quiz,
                    "night_owl_quiz": night_owl_quiz,
                    "fun_sun_quiz": fun_sun_quiz,
                    "relaxation_quiz": relaxation_quiz,
                    "shopping_quiz": shopping_quiz,
                }
            `);
        } catch (error) {
            printToOutput("Error initializing quiz: " + error);
            return;
        }
    } else {
        try {
            let pythonInput = input;
            if (input !== "") {
                pythonInput = `"${input}"`; // Enclose input in quotes for Python
            }

            const result = await pyodide.runPythonAsync(`
                import io
                import sys

                old_stdout = sys.stdout
                sys.stdout = io.StringIO()

                last_line = js.outputDiv.innerText.split('<br>').slice(-2, -1)[0]
                if last_line.includes("Enter your choice") {
                    try:
                        choice = int(${pythonInput})
                        if last_line.includes("1-8"):
                            selected_interest = list(main_interests.keys())[choice - 1]
                            main_interests[selected_interest]()
                        elif last_line.includes("1-5"):
                            # ... (rest of the if/elif logic from your original script.js) ...
                        # ...
                        elif last_line.includes("1-11"):
                            # ...
                    except (ValueError, IndexError):
                        print("Invalid input. Please enter a number.")
                }

                captured_output = sys.stdout.getvalue()
                sys.stdout = old_stdout
                js.printToOutput(captured_output)
            `);

        } catch (error) {
            printToOutput("Python Error: " + error);
        }
    }
}
loadPyodide();