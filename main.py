detective_name = "" 

def main():
    intro()
    print("\nLet's explore the case first, shall we?")
    ready = input("Type 'yes' to proceed or 'no' to exit: ")

    while ready.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        ready = input("Type 'yes' to proceed or 'no' to exit: ")

    if ready.lower() == 'yes':
        instruction()
        start_game()
    else:
        print("\n🕵️‍♀️ You step away... for now. The case remains unsolved.")
        exit()
        
def intro():
    global detective_name
    print("\n🚢 WELCOME ABOARD , THE OCEAN PEARL")
    detective_name = input("\nWhat is your name, Detective: ")
    print("\n 🔎 Welcome, Detective" , detective_name, ". A murder has occured..")
    print("\nThe ship docks in 10 hours. Can you solve the case by then??")


def instruction():
    print("\n📜 CASE BRIEFING")
    print("As Detective " , detective_name , " you're aboard The Ocean Pearl — a luxury cruise turned crime scene.")
    print("⛴️  At exactly midnight, Mr. Edward Thompson — a wealthy businessman — was found dead on the upper deck near the pool.")
    print("🩸  The crew says it was an accident, but something feels off. Too many secrets, too many suspects...")
    print("💼  Your job is to explore six key areas on the ship, interrogate people, gather clues, and find the killer.")
    print("🕒  Each action takes time. You have just 10 hours before the ship docks and the killer walks free.")
    print("\nWill you crack the case, or will the truth sink into the sea?")


def start_game():
    from scenes import start_scene
    start_scene(detective_name)


main()
