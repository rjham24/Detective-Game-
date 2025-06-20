global detective_name
from room import upper_deck, dining_hall, dj_lounge, cabins, kitchen, engine_room
from deduction import accuse

def start_scene(detective_name):
    while True:
        print("\n🌍 WHERE TO NEXT, DETECTIVE?")
        print("1. 🌊 Upper Deck")
        print("2. 🍽️ Dining Hall")
        print("3. 🎶 DJ Lounge")
        print("4. 🛏️ Cabins")
        print("5. 👨‍🍳 Kitchen")
        print("6. ⚙️ Engine Room")
        print("7. 🧠 Make an Accusation")
        print("8. 🚪 Exit Game")

        choice = input("Choose location or action: ")

        if choice == "1":
            upper_deck(detective_name)
        elif choice == "2":
            dining_hall(detective_name)
        elif choice == "3":
            dj_lounge(detective_name)
        elif choice == "4":
            cabins(detective_name)
        elif choice == "5":
            kitchen(detective_name)
        elif choice == "6":
            engine_room(detective_name)
        elif choice == "7":
            accuse()
        elif choice == "8":
            print("🕵️‍♀️ You step away... for now.")
            break
        else:
            print("Invalid input. Try again.")

