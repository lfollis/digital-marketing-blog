const outputDiv = document.getElementById('output');
const userInput = document.getElementById('user-input');

function printToOutput(text) {
    outputDiv.innerHTML += text + '\n';
    outputDiv.scrollTop = outputDiv.scrollHeight;
}

let quizState = null;

async function runPythonQuiz() {
    const input = userInput.value;
    userInput.value = '';

    if (quizState === null) {
        // Initialize Python quiz and capture functions
        quizState = await pyodide.runPythonAsync(`
import io
import sys

# ... (Your Python quiz code from previous example goes here.  No changes needed.) ...

# Capture standard output and redirect to printToOutput
old_stdout = sys.stdout
sys.stdout = io.StringIO()

tourist_attraction_quiz()

captured_output = sys.stdout.getvalue()
sys.stdout = old_stdout
js.printToOutput(captured_output)

# Return the quiz functions so they can be called later
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

    } else {
        // Subsequent turns, send input to Python and get output
        try {
            const result = await pyodide.runPythonAsync(`
                # Capture standard output and redirect to printToOutput
                old_stdout = sys.stdout
                sys.stdout = io.StringIO()

                # Get the last output to determine what function to call
                last_line = js.outputDiv.innerText.split('\\n').slice(-2, -1)[0]
                if last_line.includes("Enter your choice")){
                    choice = int("${input}")
                    
                    if last_line.includes("1-8"):
                        selected_interest = list(main_interests.keys())[choice - 1]
                        main_interests[selected_interest]()
                    elif last_line.includes("1-5"):
                        if "workout" in last_line:
                            selected_workout = list(workouts.keys())[choice - 1]
                            if selected_workout == "Crossfit":
                                js.printToOutput(workouts[selected_workout])
                            else:
                                js.printToOutput("Do you prefer working out indoors or outdoors?")
                        elif "scenery" in last_line:
                            selected_scenery = list(scenery.keys())[choice - 1]
                            js.printToOutput(scenery[selected_scenery])
                        elif "meal" in last_line:
                            selected_meal = list(meals.keys())[choice - 1]
                            meals[selected_meal]()
                        elif "preference" in last_line:
                            # Add logic to check which preference is being asked and call the appropriate function
                            if "breakfast" in last_line:
                                selected_preference = list(breakfast_preferences.keys())[choice - 1]
                                js.printToOutput(breakfast_preferences[selected_preference])
                            elif "lunch" in last_line:
                                selected_preference = list(lunch_preferences.keys())[choice - 1]
                                js.printToOutput(lunch_preferences[selected_preference])
                            elif "dinner" in last_line:
                                selected_preference = list(dinner_preferences.keys())[choice - 1]
                                js.printToOutput(dinner_preferences[selected_preference])
                            elif "tapas" in last_line:
                                selected_preference = list(tapas_preferences.keys())[choice - 1]
                                js.printToOutput(tapas_preferences[selected_preference])

                    elif last_line.includes("1-4"):
                        selected_meal = list(meals.keys())[choice - 1]
                        meals[selected_meal]()
                    elif last_line.includes("1-9"):
                        selected_vibe = list(vibes.keys())[choice - 1]
                        js.printToOutput(vibes[selected_vibe])
                    elif last_line.includes("1-2"):
                        if "indoor" in last_line:
                            indoor_outdoor = "Indoors" if choice == 1 else "Outdoors"
                            js.printToOutput(workouts[selected_workout][indoor_outdoor])
                        elif "gender" in last_line:
                            gender = "Male" if choice == 1 else "Female"
                            js.printToOutput(recommendations[(selected_shop_type, gender)])

                    elif last_line.includes("1-11"):
                        selected_shop_type = list(shopping_types.keys())[choice - 1]
                        if selected_shop_type == "Home decor":
                            js.printToOutput("You should check out Deja Vu, located at 716 La Salle Street, Ottawa, IL.")
                        else:
                            js.printToOutput("Are you looking for a male or female?")


                captured_output = sys.stdout.getvalue()
                sys.stdout = old_stdout
                js.printToOutput(captured_output)
            `);
        } catch (error) {
            printToOutput("Python Error: " + error);
        }
    }
}


async function loadPyodide() {
    await pyodide.loadPyodide({ indexURL : "https://cdn.jsdelivr.net/pyodide/v0.22.1/full/" });
    // Add any necessary Python packages here if needed.
    await pyodide.loadPackage(['micropip']);
    await pyodide.runPythonAsync('import sys; sys.stdout = io.StringIO()'); // Redirect stdout
}

loadPyodide();