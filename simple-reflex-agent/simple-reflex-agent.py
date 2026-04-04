goalState  = {'A': '0', 'B': '0', 'C': '0'}
roomStates = {'A': '0', 'B': '0', 'C': '0'}
cost = 0

// simple reflex agent for vacuum cleaner problem
def get_location_input():
    """Keep asking until user enters a valid starting location (A, B, or C)."""
    valid = ['A', 'B', 'C']
    while True:
        loc = input("Enter the starting location of vacuum (A / B / C): ").strip().upper()
        if loc in valid:
            return loc
        print(f"  ❌ Invalid input '{loc}'. Location must be A, B, or C. Please try again.\n")


def get_status_input(room):
    """Keep asking until user enters a valid room status (0 or 1)."""
    valid = ['0', '1']
    while True:
        status = input(f"Enter the state of {room} (0 for clean / 1 for dirty): ").strip()
        if status in valid:
            return status
        print(f"  ❌ Invalid input '{status}'. Status must be 0 (clean) or 1 (dirty). Please try again.")

print("=" * 55)
print("       TASK 2 – Simple Reflex Agent")
print("=" * 55)
print()

location = get_location_input()

print()
for room in roomStates:
    roomStates[room] = get_status_input(room)
print()
print("\nCurrent State : " + str(roomStates))
print("Goal State    : " + str(goalState))
print("Vacuum placed at location: " + location)

if roomStates == goalState:
    print("\nAll rooms are already clean.")

    print("Total cost: " + str(cost))
else:
    ROOM_ORDER = ['A', 'B', 'C']
    start_idx  = ROOM_ORDER.index(location)
    current    = location

    for room in ROOM_ORDER[start_idx:]:

        if room != current:
            print(f"\nRoom {current} is clean. Moving {current} → {room}")
            cost += 1
            print(f"Cost for moving = 1.  Running total: {cost}")
            current = room

        if roomStates[room] == '1':
            roomStates[room] = '0'
            cost += 1
            print(f"\nRoom {room} was dirty. Cleaned successfully.")
            print(f"Cost for cleaning = 1.  Running total: {cost}")
        else:
            print(f"\nRoom {room} is already clean. No action needed.")


        if roomStates == goalState:
            print("\nGoal state has been met.")
            print("Total cost: " + str(cost))
            break

    else:
        if roomStates == goalState:
            print("\nGoal state has been met.")
        else:
            print("\nGoal state NOT fully reached (rooms before start location were not visited).")
        print("Total cost: " + str(cost))