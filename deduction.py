from tracker import all_areas_visited, show_clues, can_accuse
from suspects import suspects , show_suspects

def accuse():
    print("\n🧠 Time to make your deduction...")
    print("You have 3 attempts to accuse the killer.")
    print("Make sure you've explored all areas and gathered enough clues before proceeding.\n")

    if not all_areas_visited():
        print("🛑 You must explore all six areas before making your final accusation.")
        return

    if not can_accuse():
        print("⚠️ You don't have enough clues to accuse anyone yet.")
        print("📌 Explore more locations and gather stronger evidence.\n")
        return

    remaining_attempts = 3
    correct_killer = "Ms. Green"

    innocence_reasons = {
        "Mr. Blue: Though his behavior is shady, his motive is financial, not emotional or violent. All evidence points to panic, not guilt."
        "Ms. Thompson: She was in the dining hall with witnesses. Her alibi is solid, and she has no motive."
        "Chef Marco: He has a motive, but his alibi checks out. The missing knife is suspicious, but he claims it was an accident."
        "DJ Echo: He was busy with the music and has no motive. His statement about seeing Mr. Blue arguing with the victim is credible."
        "Steward Roy: His clue was there to build tension — he has no connection to the victim or motive to kill."
    }

    while remaining_attempts > 0:
        print("\n🔍 You have " , remaining_attempts , " attempt(s) left.")
        print("\nHere are the suspects:")
        for name in suspects.keys():
            print("-" , name)

        selected_name = input("\nWho do you accuse? Type their full name exactly: ").strip()
        remaining_attempts -= 1

        if selected_name == correct_killer:
            print("\n✅ You solved the case!")
            print("💬 Ms. Green breaks down: 'He betrayed my best friend, and had an affair with his colleague , he thought he’d get away with it!'")
            print("🎉 Congratulations, Detective! You caught the killer before the ship docked.")
            break
        elif selected_name in suspects:
            reason = innocence_reasons.get(selected_name)
            print("❌" , selected_name , " is not the killer.")
            print("🧩", reason)
            print("Try again.")
        else:
            print("⚠️ Name not recognized. Try typing one from the list.")

    print("\n🔍 You've used all your attempts!")
    print("The killer was: " , correct_killer)
    print("💬 Ms. Green smirks as she walks away... maybe next time, Detective.")