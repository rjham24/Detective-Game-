suspects = {
    "Ms. Green": {
        "role": "Passenger",
        "alibi": "Claims she saw a crew member near the pool at midnight",
        "truth": True,
        "motive": "Jealousy over Mr. Thompson's popularity",
        "connected_clues": [
            "Ms. Green: Saw a shadowy figure near the pool — thought it was a crew member.",
            "Clue: Crumpled receipt for a 12:05 AM drink found under Ms. Green’s table"
        ],
        "rumors": [
            "She’s always been quiet — but some say she saw the argument and said nothing.",
            "Was unusually friendly with the victim a few nights ago."
        ]
    },

    "Mr. Blue": {
        "role": "Passenger",
        "alibi": "Was in his cabin",
        "truth": False,
        "motive": "Financial debt to victim",
        "connected_clues": [
            "Suspect Statement: Mr. Blue claims he was in his cabin at the time",
            "Clue: DJ Statement: Saw a man arguing with the victim earlier",
            "Clue: Mr. Blue’s jacket found in DJ Lounge with torn cuff matching fabric from Cabin 206"
        ],
        "rumors": [
            "Mr. Blue once accused Mr. Thompson of cheating in cards... they had tension last night.",
            "He was seen sneaking out of the engine room once before."
        ]
    },

    "Ms. Thompson": {
        "role": "Wife of victim",
        "alibi": "Claims she was in her room",
        "truth": False,
        "motive": "Marital conflict, jealousy",
        "connected_clues": [
            "Clue: Torn cruise schedule with room number 204 smeared red lipstick found near deck chair",
            "Clue: Wife's lipstick is smudged — suspiciously similar to the napkin in the dining hall."
        ],
        "rumors": [
            "They were fighting loudly in the hallway earlier that day.",
            "She once threw a drink at Mr. Thompson at a party last year."
        ]
    },

    "Chef Marco": {
        "role": "Head Chef",
        "alibi": "In kitchen",
        "truth": True,
        "motive": "Argument with victim",
        "connected_clues": [
            "Chef Statement: Argued with victim earlier",
            "Clue: Blood-stained tissue near kitchen trash",
            "Clue: Large kitchen knife missing from kitchen"
        ],
        "rumors": [
            "He got a warning last cruise for shouting at a guest.",
            "Some say he lost a promotion because of Mr. Thompson’s complaint."
        ]
    },

    "DJ Echo": {
        "role": "Lounge DJ",
        "alibi": "Playing music",
        "truth": True,
        "motive": "None",
        "connected_clues": [],
        "rumors": [
            "He’s a gossip — always knows who’s sneaking around.",
            "Claims he saw ‘someone crying’ near the cabins before midnight."
        ]
    },

    "Steward Roy": {
        "role": "Crew Member",
        "alibi": "Claims he was cleaning the lower deck after midnight",
        "truth": True,
        "motive": "None directly — but known for careless mistakes",
        "connected_clues": [
            "Clue: Access card left logged in at midnight — belonged to steward Roy.",
            "Log: Engine Room accessed at 12:03 AM"
        ],
        "rumors": [
            "Roy’s been written up before for leaving doors unlocked.",
            "Someone saw Roy drop his keycard near the DJ lounge entrance."
        ]
    }
}


def show_suspects(show_rumors=True):
    print("\n🧍 SUSPECT LIST:\n")
    for name, data in suspects.items():
        print("Name:", name)
        print("Role:", data['role'])
        print("Alibi:", data['alibi'])
        print("Motive:", data['motive'])
        print("Related Clues:")
        for clue in data['connected_clues']:
            print(" -", clue)
        if show_rumors:
            print("Rumors:")
            for r in data['rumors']:
                print(f"   🗣️ {r}")
        print()
