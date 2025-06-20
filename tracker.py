time_left = 10
clues = []

def use_time(hours = 1):
    global time_left
    time_left -= hours
    print("\n 🕒" , hours , "hour(s) passed. Time Remaining" , time_left )
    if time_left <= 0:
        print("🛑 Time's up! The case remains unsolved.")
        exit()

def add_clue(clue):
    if clue not in clues:
        clues.append(clue)
        print ("📝 Clue added:" , clue)
    else:
        print("Clue already exists:")

def show_clues():
      print("\n📂 Your Case Notes:")
      if clues:
          for clue in clues:
              print(" -", clue)
      else:
            print("No clues found yet. Keep investigating!")

def get_time_left():
    return time_left

def can_accuse():
    return len(clues) >= 7 

visited_areas = set()

def mark_area_visited(area):
    visited_areas.add(area)

def all_areas_visited():
    return len(visited_areas) >= 6

