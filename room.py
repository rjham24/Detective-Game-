from tracker import use_time , add_clue , show_clues

def upper_deck(detective_name):
    use_time()
    from tracker import mark_area_visited
    mark_area_visited("Upper Deck")
    print("\n 🌊 Upper Deck - Midnight Breeze")
    print("The moonlight shimmers on the ocean , Detective ", detective_name, ".")
    print("A body lies near the pool , lifeless and cold, surround by a security tape. The crew is in shock.\n")
    while True:
        print("\n🕵️‍♂️ You must investigate the scene. What will you do?")
        print("1. Examine the body")
        print("2. Talk to the crew")
        print("3. Look around the deck for clues")
        print("4. Check your case notes")
        print("5. Leave the scene")

        choice = input("\nChoose your action: ")

        if choice == "1":
            print("\n🩺 You examine the body.")
            print("There was a knife in his chest, and a broken wristwatch in hand")
            add_clue("Victim: Mr. Thompson - Knife in chest, broken wristwatch")

        elif choice == "2":
            print("\n👥 You talk to the crew. They are shaken but cooperative.")
            print("Guard says : 'Security tape was removed after the midnight for privacy. ")
            add_clue("Crew Statement: Security tape removed after midnight")

        elif choice == "3":
            print("\n🔍 You scan the deck carefully. Something catches your eye near a deck chair.")
            print("It's a torn page from a cruise schedule with room number labelled 204  — with smeared red lipstick.")
            add_clue("Clue: Torn cruise schedule with room number 204 smeared red lipstick found near deck chair")

        
        elif choice == "4":
            show_clues()    

        elif choice == "5":
            print("\n🚪 You leave the scene, but the mystery remains unsolved.")
            break

        else:
            print("Invalid choice. Please try again.")


def dining_hall(detective_name):
    use_time()
    from tracker import mark_area_visited
    mark_area_visited("Dining Hall")
    print("\n 🍽️ Dining Hall - A Taste of Suspicion")
    print("The dining hall is bustling with activity, Detective", detective_name, ".")
    print("Passengers are tensed. You notice a few suspects.")     
    while True:
        print("\n🕵️‍♂️ You must gather information. What will you do?")
        print("1. Interrogate the suspects")
        print("2. Search for clues")
        print("3. Check your case notes")
        print("4. Leave the dining hall")


        choice = input("\nChoose your action: ")

        if choice == "1":
            print("\n👮 You interrogate the suspects. They seem nervous, but one of them slips up.")
            print("A passenger named Ms. Green mentions seeing someone near the crime scene at midnight.")
            add_clue("Ms. Green: Saw a shadowy figure near the pool — thought it was a crew member.")

        elif choice == "2":
            print("\n🔎 While scanning the dining area, you find a crumpled receipt near Ms. Green’s usual table.")
            print("It’s for a drink ordered at 12:05 AM — well past curfew, when the dining hall should've been closed.")
            add_clue("Clue: Crumpled receipt for a 12:05 AM drink found under Ms. Green’s table")

        elif choice == "3":
            show_clues()      

        elif choice == "4":
            print("\n🚪 You leave the dining hall, but the mystery deepens.")
            break
            
        else:
            print("Invalid choice. Please try again.")  


def dj_lounge(detective_name):
    use_time()
    from tracker import mark_area_visited
    mark_area_visited("DJ Lounge")
    print("\n 🎶 DJ Lounge - Beats of Deception")
    print("The DJ lounge is lively, Detective", detective_name, ".")
    print("Music is pumping, and the atmosphere is electric. You see a few suspects mingling.")
    while True:
        print("\n🕵️‍♂️ You must gather information. What will you do?")
        print("1. Talk to the DJ")
        print("2. Interrogate a suspect")
        print("3. Search for clues")
        print("4. Check your case notes")
        print("5. Leave the DJ lounge")

        choice = input("\nChoose your action: ")

        if choice == "1":
            print("\n🎧 You talk to the DJ. He seems relaxed but mentions something odd.")
            print("He saw a man arguing with the victim earlier in the night.")
            add_clue("DJ Statement: Saw a man arguing with the victim earlier")

        elif choice == "2":
            print("\n👤 You interrogate Mr. Blue who was using his phone in the lounge. They seem nervous but provide some information.")
            print("Mr. Blue claims he was in his cabin at the time .")
            add_clue("Suspect Statement: Mr. Blue claims he was in his cabin at the time")      

        elif choice == "3":
            print("\n🔍 You search the DJ lounge carefully.")
            print("Behind a seat, you find a crumpled coat — a dark jacket with a torn cuff, matching the fabric found near Cabin 206.")
            add_clue("Clue: Mr. Blue’s jacket found in DJ Lounge with torn cuff matching fabric from Cabin 206")

        elif choice == "4":
            show_clues()  

        elif choice == "5":
            print("\n🚪 You leave the DJ lounge, but the mystery remains unsolved.")
            break

        else:
            print("Invalid choice. Please try again.")  


def cabins(detective_name):
    use_time()
    from tracker import mark_area_visited
    mark_area_visited("Cabins")
    print("\n 🛏️ Cabins - Secrets Behind Closed Doors")
    print("The cabins are quiet, Detective", detective_name, ".")
    print("You see a few doors, and the atmosphere is tense. You must choose wisely.")
    while True:
        print("\n🕵️‍♂️ You must gather information. What will you do?")
        print("1. Knock on a cabin door 204 ")
        print("2. Search for clues in the hallway")
        print("3. Check your case notes")
        print("4. Leave the cabins")

        choice = input("\nChoose your action: ")

        if choice == "1":
            print("\n🚪 You knock on a cabin door 204 . A passenger answers, looking nervous.")
            print(" The passenger was the wife of the victim, Ms. Thompson.")
            print("She claims she was in her room at the time of murder but her lipstick is smudged.")
            add_clue("Clue: Wife's lipstick is smudged — suspiciously similar to the napkin in the dining hall.")

        elif choice == "2":
            print("\n🔎 You search for clues in the hallway. The area is quiet, but you find something.")
            print("You discover a torn piece of dark fabric caught on the door handle of Cabin 206 — Mr. Blue’s room is wide open.")
            add_clue("Clue: Torn dark fabric caught on Mr. Blue’s cabin (206) door handle")

        elif choice == "3":
            show_clues()       

        elif choice == "4":
            print("\n🚪 You leave the cabins, but the mystery remains unsolved.")
            break

        else:
            print("Invalid choice. Please try again.")

def kitchen(detective_name):
    use_time()
    from tracker import mark_area_visited
    mark_area_visited("Kitchen")
    print("\n👩‍🍳 Kitchen – A Recipe for Secrets")
    print("The kitchen smells of spices and tension, Detective " , detective_name , ".")
    print("Chefs rush about, but something feels off.")

    while True:
        print("\n🕵️‍♂️ What will you do?")
        print("1. Interrogate the head chef")
        print("2. Check the knife inventory")
        print("3. Look around for clues")
        print("4. Check your case notes")
        print("5. Leave the kitchen")

        choice = input("\nChoose your action: ")

        if choice == "1":
            print("\n👨‍🍳 The head chef seems angry.")
            print("'That man ruined my special — and now this mess!'")
            print("He admits the victim had an argument with the chef earlier.")
            add_clue("Chef Statement: Argued with victim earlier")

        elif choice == "2":
            print("\n🔪 You inspect the knife set.")
            print("One large kitchen knife is missing.")
            add_clue("Clue: Large kitchen knife missing from kitchen")

        elif choice == "3":
            print("\n🔍 You spot blood-stained tissue near the trash bin.")
            add_clue("Clue: Blood-stained tissue near kitchen trash")

        elif choice == "4":
            show_clues()

        elif choice == "5":
            print("\n🚪 You leave the kitchen. The heat still lingers.")
            break

        else:
            print("Invalid choice. Try again.")

def engine_room(detective_name):
    use_time()
    from tracker import mark_area_visited
    mark_area_visited("Engine Room")
    print("\n⚙️ Engine Room – Machinery and Mystery")
    print("The engine roars beneath your feet, Detective", detective_name , ".")
    print("It’s loud, greasy, and suspiciously empty.")

    while True:
        print("\n🕵️‍♂️ What will you do?")
        print("1. Check the toolbox")
        print("2. Search the control panel")
        print("3. Look around for strange marks")
        print("4. Check your case notes")
        print("5. Leave the engine room")

        choice = input("\nChoose your action: ")

        if choice == "1":
            print("\n🧰 You find scratch marks on the inside of the toolbox lid.")
            add_clue("Clue: Scratches inside toolbox")

        elif choice == "2":
            print("\n💻 Control panel logs show an unusual access at 12:03 AM.")
            add_clue("Log: Engine Room accessed at 12:03 AM")
            add_clue("Clue: Access card left logged in at midnight — belonged to steward Roy.")

        elif choice == "3":
            print("\n🛠 You notice greasy handprints on the door, leading outside.")
            add_clue("Clue: Greasy handprints lead out of engine room")

        elif choice == "4":
            show_clues()

        elif choice == "5":
            print("\n🚪 You exit the engine room. The mystery deepens.")
            break

        else:
            print("Invalid choice. Try again.")