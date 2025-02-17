def tourist_attraction_quiz():
    print("Welcome to the Ottawa Tourist Attraction Quiz!")

    main_interests = {
        "Fitness warrior": fitness_quiz,
        "Outdoor explorer": outdoor_quiz,
        "Foodie": foodie_quiz,
        "Night Owl": night_owl_quiz,
        "Fun & sun": fun_sun_quiz,
        "Relaxation": relaxation_quiz,
        "Shop-a-holic": shopping_quiz
    }

    print("What do you like to do?")
    for i, interest in enumerate(main_interests):
        print(f"{i+1}. {interest}")

    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= len(main_interests):
                selected_interest = list(main_interests.keys())[choice - 1]
                main_interests[selected_interest]()
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def fitness_quiz():
    workouts = {
        "Crossfit": "You should check out Crossfit 360, located at 711 West Joliet Street, Ottawa, IL.",
        "Aerobic": {"Indoors": "You should check out the YMCA, located at 411 Canal Street, Ottawa, IL.",
                    "Outdoors": "You should check out the I&M Canal, located near Fox River Park, on the northside of East Superior Street."},
        "Strength-training": {"Indoors": "You should check out JJR Next Level, located at 815 La Salle Street, Ottawa, IL.",
                             "Outdoors": "You should check out The Fitness Court, located at 115 East Glover Street, Ottawa, IL."},
        "Running/walking/biking": {"Indoors": "You should check out JJR Next Level, located at 815 La Salle Street, Ottawa, IL.",
                                 "Outdoors": "You should check out You should check out the I&M Canal, located near Fox River Park, on the northside of East Superior Street."},
        "Yoga": {"Indoors": "You should check out EnergYoga, located at 225 West Madison Street, Ottawa, IL.",
                 "Outdoors": "You should check out Nells Woodland, located at 2000 Alexis Avenue, Ottawa, IL."}
    }

    print("What type of workouts do you enjoy?")
    for i, workout in enumerate(workouts):
        print(f"{i+1}. {workout}")

    while True:
      try:
        workout_choice = int(input("Enter your choice (1-5): "))
        if 1 <= workout_choice <= len(workouts):
            selected_workout = list(workouts.keys())[workout_choice - 1]

            if selected_workout == "Crossfit":
                print(workouts[selected_workout])
                break

            print("Do you prefer working out indoors or outdoors?")
            print("1. Indoors")
            print("2. Outdoors")

            while True:
              try:
                indoor_choice = int(input("Enter your choice (1-2): "))
                if 1 <= indoor_choice <= 2:
                  indoor_outdoor = "Indoors" if indoor_choice == 1 else "Outdoors"
                  print(workouts[selected_workout][indoor_outdoor])
                  break
                else:
                  print("Invalid choice. Please enter 1 or 2.")
              except ValueError:
                print("Invalid input. Please enter a number.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
      except ValueError:
        print("Invalid input. Please enter a number.")


def outdoor_quiz():
    scenery = {
        "River route": "You should check out Starved Rock National Park and hike to LaSalle Canyon, located at 2678 East 873 Road, Oglesby, IL.",
        "Waterfall": "You should check out Mattheissen Park and hike to Lake Falls, located at 2500 IL-178, Oglesby, IL.",
        "Aerial views": "You should check out Starved Rock National Park and hike to Lover’s Leap, located at 2678 East 873 Road, Oglesby, IL.",
        "Buffalo": "You should check out Buffalo Rock State Park, located off Dee Bennett Road, Ottawa, IL.",
        "Nature walk": "You should check out the Dayton Bluff Preserves, located at 2997 IL-71, Ottawa, IL."
    }

    print("What scenery are you looking for?")
    for i, option in enumerate(scenery):
        print(f"{i+1}. {option}")

    while True:
      try:
        choice = int(input("Enter your choice (1-5): "))
        if 1 <= choice <= len(scenery):
            selected_scenery = list(scenery.keys())[choice - 1]
            print(scenery[selected_scenery])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
      except ValueError:
        print("Invalid input. Please enter a number.")

def foodie_quiz():
    meals = {
        "Breakfast": breakfast_quiz,
        "Lunch": lunch_quiz,
        "Dinner": dinner_quiz,
        "Tapias/snacks": tapas_snacks_quiz
    }

    print("What are you eating?")
    for i, meal in enumerate(meals):
        print(f"{i+1}. {meal}")

    while True:
      try:
        choice = int(input("Enter your choice (1-4): "))
        if 1 <= choice <= len(meals):
            selected_meal = list(meals.keys())[choice - 1]
            meals[selected_meal]()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
      except ValueError:
        print("Invalid input. Please enter a number.")



def breakfast_quiz():
    preferences = {
        "Quick and friendly service": "You should check out The HiWay Restaurant, located at 210 West Norris Drive, Ottawa, IL.",
        "Lots of options": "You should check out The New Brite Spot Family Restaurant, located at 801 East Norris Drive, Ottawa, IL.",
        "Cafe style": "You should check out Garden Berry Cafe, located at 711 La Salle Street, Ottawa, IL."
    }
    print("Tell us your preference:")
    for i, pref in enumerate(preferences):
        print(f"{i+1}. {pref}")

    while True:
      try:
        choice = int(input("Enter your choice (1-3): "))
        if 1 <= choice <= len(preferences):
            selected_preference = list(preferences.keys())[choice - 1]
            print(preferences[selected_preference])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
      except ValueError:
        print("Invalid input. Please enter a number.")

def lunch_quiz():
    preferences = {
        "American": "You should check out Halftime Restaurant, Pizza & Cocktails, located at 1625 East Norris Drive, Ottawa, IL.",
        "Mexican": "You should check out Fiesta MX, located at 221 West Madison Street, Ottawa, IL.",
        "Thai": "You should check out The Thai Cafe, located at 610 Columbus Street, Ottawa, IL.",
        "Chinese": "You should check out Dragon City, located at 517 East Norris Drive, Ottawa, IL.",
        "Bar & Grill": "You should check out Shakers Sports Bar & Grill, located at 121 West Stevenson Road, Ottawa, IL.",
        "Pizza": "You should check out Bianchi’s North, located at 217 East Norris Drive, Ottawa, IL.",
        "Deli": "You should check out The Cheese Shoppe and Deli, located at 1219 Fulton Street, Ottawa, IL."
    }

    print("Tell us your preference:")
    for i, pref in enumerate(preferences):
        print(f"{i+1}. {pref}")

    while True:
      try:
        choice = int(input("Enter your choice (1-7): "))
        if 1 <= choice <= len(preferences):
            selected_preference = list(preferences.keys())[choice - 1]
            print(preferences[selected_preference])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
      except ValueError:
        print("invalid")

def dinner_quiz():
    preferences = {
        "American": "You should check out Anne’s Hideaway, located at 323 West Railroad Avenue, Ottawa, IL.",
        "Steak House": "You should check out Woody’s Steak House, located at 1321 LaSalle Street, Ottawa, IL.",
        "Seafood": "You should check out The Beach House, located at 700 LaSalle Street, Ottawa, IL.",
        "Sushi": "You should check out Burger and Sushi House, located at 1012 La Salle St, Ottawa, IL.",
        "Burgers": "You should check out The Bears Den, located at 1607 Ottawa Avenue, Ottawa, IL.",
        "Dinner with a view": "You should check out Bluegill Boathouse, located at 411 Great Loop East Drive, Ottawa, IL.",
        "Mexican": "You should check out Mariachis, located at 1911 Ottawa Avenue, Ottawa, IL.",
        "Pizza": "You should check out Iniga Pizzeria Napoletana, located at 215 West Jefferson Street, Ottawa, IL."
    }

    print("Tell us your preference:")
    for i, pref in enumerate(preferences):
        print(f"{i+1}. {pref}")

    while True:
      try:
        choice = int(input("Enter your choice (1-8): "))
        if 1 <= choice <= len(preferences):
            selected_preference = list(preferences.keys())[choice - 1]
            print(preferences[selected_preference])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
      except ValueError:
        print("Invalid input. Please enter a number.")


def tapas_snacks_quiz():
    preferences = {
        "Bar food": "You should check out Bertas Tap, located at 616 Clinton Street, Ottawa, IL.",
        "Wings": "You should check out Vegas Wings, located at 309 East McKinley Road, Ottawa, IL.",
        "Beef rolls": "You should check out Pizza by Marchelloni, located at 424 West Main Street, Ottawa, IL.",
        "Nachos": "You should check out Mr. J’s Hot Dogs & Gyros, located at 1118 Columbus Street, Ottawa, IL.",
        "Large pretzels": "You should check out Court Street Pub, located at 620 Court Street, Ottawa, IL.",
        "Mediterranean": "You should check out Saffron Bazaaril, located at 1409 LaSalle Street, Ottawa, IL."
    }

    print("Tell us your preference:")
    for i, pref in enumerate(preferences):
        print(f"{i+1}. {pref}")

    while True:
      try:
        choice = int(input("Enter your choice (1-6): "))
        if 1 <= choice <= len(preferences):
            selected_preference = list(preferences.keys())[choice - 1]
            print(preferences[selected_preference])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
      except ValueError:
        print("Invalid input. Please enter a number.")

def night_owl_quiz():
    vibes = {
        "Casual/relaxed": "You should check out Bertas Tap, located at 616 Clinton Street, Ottawa, IL.",
        "Large crowds": "You should check out Court Street Pub, located at 620 Court Street, Ottawa, IL.",
        "Dancing": "You should check out Shakers Sports Bar & Grill, located at 121 West Stevenson Road, Ottawa, IL.",
        "Wine night": "You should check out CatsEye Wine Bar, located at 724 La Salle Street, Ottawa, IL.",
        "Roller skating": "You should check out Paramount Skating Arena, located at 1511 Chestnut Street, Ottawa, IL.",
        "Slot machines": "You should check out Cats Q BBQ, located at 1137 W Main Street, Ottawa, IL.",
        "Singles hot-spot": "You should check out Bar Stars, located at 620 W Madison Street, Ottawa, IL.",
        "Local Dive Bar": "You should check out The Bears Den, located at 1607 Ottawa Avenue, Ottawa, IL.",
        "On the water": "You should check out Dockside Bar & Grill, located at 1001 E. Main, Ottawa, IL."
    }

    print("What’s the vibe?")
    for i, vibe in enumerate(vibes):
        print(f"{i+1}. {vibe}")

    while True:
      try:
        choice = int(input("Enter your choice (1-9): "))
        if 1 <= choice <= len(vibes):
            selected_vibe = list(vibes.keys())[choice - 1]
            print(vibes[selected_vibe])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
      except ValueError:
        print("Invalid input. Please enter a number.")


def fun_sun_quiz():
    activities = {
        "Explore the Illinois River": "You should check out Heritage Harbor Marina, located at 421 Great Loop E Drive, Ottawa, IL.",
        "Explore the Fox River": "You should check out Ayers Landing Canoes, Tubes and Kayaks, located at 3494 E 2089th Road, Wedron, IL.",
        "Explore the Vermillion River": "You should check out Starved Rock River Adventures, located at 1132 N 27th Road, Ottawa, IL.",
        "Swim": "You should check out Riordan Pool, located at 600 Utica Drive, Ottawa, IL.",
        "Splash Pad": "You should check out Thorton Park, located at 1600 West Jackson Street, Ottawa, IL.",
        "Golf": "You should check out Pine Hills Golf Club & Restaurant, located at 1665 N 2501st Road, Ottawa, IL.",
        "Disc golf": "You should check out Fox River Park, located at 717 Hudson Street, Ottawa, IL.",
        "Picnic": "You should check out Buffalo Rock State Park, located off Dee Bennett Road, Ottawa, IL.",
        "Bike": "You should check out The Bike Shop, located at 1313 Chestnut Street, Ottawa, IL."
    }

    print("What would you like to do?")
    for i, activity in enumerate(activities):
        print(f"{i+1}. {activity}")

    while True:
      try:
        choice = int(input("Enter your choice (1-9): "))
        if 1 <= choice <= len(activities):
            selected_activity = list(activities.keys())[choice - 1]
            print(activities[selected_activity])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
      except ValueError:
        print("Invalid input. Please enter a number.")


def relaxation_quiz():
    zen_options = {
        "Meditation": "You should check out One Rive Zen, located at 121 East Prospect Avenue, Ottawa, IL.",
        "Massage": "You should check out MAC Therapy: Massage and Corrective Therapy, located at 612 Fillmore Street, Ottawa, IL.",
        "Yoga": "You should check out EnergYoga, located at 225 W Madison St, Ottawa, IL.",
        "Natural Healing": "You should check out Salt Tree Yoga, located at 310 1/2 W Main St Second Floor, Ottawa, IL.",
        "Day Spa": "You should check out LIV Wellness Lounge, located at 827 East Norris Drive, Ottawa, IL.",
        "Reading": "You should check out Prairie Fox Books, located at 719 La Salle Street, Ottawa, IL.",
        "Winery": "You should check out August Hill Winery, located at 106 Mill Street, North Utica, IL."
    }

    print("Choose your Zen:")
    for i, zen in enumerate(zen_options):
        print(f"{i+1}. {zen}")

    while True:
      try:
        choice = int(input("Enter your choice (1-7): "))
        if 1 <= choice <= len(zen_options):
            selected_zen = list(zen_options.keys())[choice - 1]
            print(zen_options[selected_zen])
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
      except ValueError:
        print("Invalid input. Please enter a number.")


def shopping_quiz():
    shopping_types = {
        "Stylish & trendy": "Stylish & trendy",  # Key is used later
        "High-end Retail": "High-end Retail",  # Key is used later
        "Sporty": "Sporty",  # Key is used later
        "Work-casual": "Work-casual",  # Key is used later
        "Plus-size": "Plus-size",  # Key is used later
        "Unique": "Unique",  # Key is used later
        "Kids": "Kids",  # Key is used later
        "Shoes": "Shoes",  # Key is used later
        "Special occasion": "Special occasion",  # Key is used later
        "Discount & thrift": "Discount & thrift",  # Key is used later
        "Home decor": "Home decor"
    }

    print("What are you shopping for?")
    for i, shop_type in enumerate(shopping_types):
        print(f"{i+1}. {shop_type}")

    while True:
      try:
        choice = int(input("Enter your choice (1-11): "))
        if 1 <= choice <= len(shopping_types):
            selected_shop_type = list(shopping_types.keys())[choice - 1]

            if selected_shop_type == "Home decor":
                print("You should check out Deja Vu, located at 716 La Salle Street, Ottawa, IL.")
                break

            print("Are you looking for a male or female?")
            print("1. Male")
            print("2. Female")

            while True:
              try:
                gender_choice = int(input("Enter your choice (1-2): "))
                if 1 <= gender_choice <= 2:
                  gender = "Male" if gender_choice == 1 else "Female"

                  # Using dictionary lookup for simplicity (no if/else chain)
                  recommendations = {
                      ("Stylish & trendy", "Female"): "You should check out Iconic Boutique, located at 617 La Salle Street, Ottawa, IL.",
                      ("Stylish & trendy", "Male"): "You should check out the That Guy’s Secret, located at 105 Marquette Street Suite B, La Salle, IL.",
                      ("High-end Retail", "Female"): "You should check out Lady Di’s, located at 717 La Salle Street, Ottawa, IL.",
                      ("High-end Retail", "Male"): "You should check out That Guy’s Secret, located at 105 Marquette Street Suite B, La Salle, IL.",
                      ("Sporty", "Male"): "You should check out Hibbett Sports, located at 2740 Columbus Street, Ottawa, IL.",
                      ("Sporty", "Female"): "You should check out Hibbett Sports, located at 2740 Columbus Street, Ottawa, IL.",
                      ("Work-casual", "Female"): "You should check out Maurices, located at 381 Stevenson Road, Ottawa, IL.",
                      ("Work-casual", "Male"): "You should check out Vlastnik’s Mensware, located at 1809 4th Street, Peru, IL.",
                      ("Plus-size", "Female"): "You should check out Bold & Curvy Boutique, located at 211 West Madison Street, Ottawa, IL.",
                      ("Plus-size", "Male"): "You should check out That Guy’s Secret, located at 105 Marquette Street Suite B, La Salle, IL.",
                      ("Unique", "Male"): "You should check out PersonaliTees, located at 721 La Salle Street, Ottawa, IL.",
                      ("Unique", "Female"): "You should check out PersonaliTees, located at 721 La Salle Street, Ottawa, IL.",
                      ("Kids", "Male"): "You should check out RPS Toys, located at 820 La Salle Street, Ottawa, IL.",
                      ("Kids", "Female"): "You should check out RPS Toys, located at 820 La Salle Street, Ottawa, IL.",
                      ("Shoes", "Male"): "You should check out Shoe Department, located at 389 West Stevenson Road, Ottawa, IL.",
                      ("Shoes", "Female"): "You should check out Shoe Department, located at 389 West Stevenson Road, Ottawa, IL.",
                      ("Special occasion", "Female"): "You should check out Marien Mae Bridal Boutique, located at 749 First Street, La Salle, IL.",
                      ("Special occasion", "Male"): "You should check out Vlastnik’s Mensware, located at 1809 4th Street, Peru, IL.",
                      ("Discount & thrift", "Male"): "You should check out Lily Pads, located at 411 East Stevenson Road, Ottawa, IL.",
                      ("Discount & thrift", "Female"): "You should check out Lily Pads, located at 411 East Stevenson Road, Ottawa, IL."
                  }

                  print(recommendations[(selected_shop_type, gender)])
                  break
                else:
                  print("Invalid choice. Please enter 1 or 2.")
              except ValueError:
                print("Invalid input. Please enter a number.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")
      except ValueError:
        print("Invalid input. Please enter a number.")