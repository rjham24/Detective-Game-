from tracker import all_areas_visited, show_clues, can_accuse
from suspects import suspects , show_suspects

def accuse():
    print("\n🧠 Time to make your deduction...")

    if not all_areas_visited():
        print("🛑 You must explore all six areas before making your final accusation.")
        return

    if not can_accuse():
        print("⚠️ You don't have enough clues to accuse anyone yet.")
        print("📌 Explore more locations and gather stronger evidence.\n")
        return

    attempts = 0
    correct_killer = "Ms. Green"

    while True:
        print("\nHere are the suspects:")
        for name in suspects.keys():
            print("-" , name)

        selected_name = input("\nWho do you accuse? Type their full name exactly: ").strip()
        attempts += 1

        if selected_name == correct_killer:
            print("\n✅ You solved the case!")
            print("💬 Ms. Green breaks down: 'He betrayed my best friend, and thought he’d get away with it!'")
            print(f"🎯 It took you {attempts} attempt(s), but justice is served.")
            break
        elif selected_name in suspects:
            print("❌ That doesn't add up. Recheck your clues and try again.")
        else:
            print("⚠️ Name not recognized. Try typing one from the list.")