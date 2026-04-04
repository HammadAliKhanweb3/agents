my_table = {

    ('A', 'Clean')                                        : 'Move Right',
    ('A', 'Dirty')                                        : 'Remove the dirt',
    ('B', 'Dirty')                                        : 'Remove the dirt',
    ('B', 'Clean')                                        : 'Move Left',


    (('A', 'Clean'), ('A', 'Clean'))                      : 'Move Right',
    (('A', 'Clean'), ('A', 'Dirty'))                      : 'Remove the dirt',
    (('B', 'Dirty'), ('B', 'Dirty'))                      : 'Remove the dirt',
    (('B', 'Dirty'), ('B', 'Clean'))                      : 'Move Left',
    (('A', 'Dirty'), ('A', 'Dirty'))                      : 'Remove the dirt',
    (('A', 'Dirty'), ('A', 'Clean'))                      : 'Move Right',


    (('A', 'Clean'), ('A', 'Clean'), ('B', 'Dirty'))      : 'Remove the dirt',
    (('A', 'Clean'), ('A', 'Dirty'), ('A', 'Clean'))      : 'Move Right',
}


def lookup_table(percept_sequence, table):
    return table.get(percept_sequence, 'No action defined for this percept sequence')


def table_driven_agent(percept_sequence):
    return lookup_table(percept_sequence, my_table)


def get_location_input():
    """Keep asking until user enters a valid location (A or B)."""
    valid = ['A', 'B']
    while True:
        loc = input("  Enter location (A / B): ").strip().upper()
        if loc in valid:
            return loc
        print(f"  ❌ Invalid input '{loc}'. Location must be 'A' or 'B'. Please try again.")


def get_status_input(location):
    """Keep asking until user enters a valid status (Clean or Dirty)."""
    valid = ['Clean', 'Dirty']
    while True:
        status = input(f"  Enter status for {location} (Clean / Dirty): ").strip().capitalize()
        if status in valid:
            return status
        print(f"  ❌ Invalid input '{status}'. Status must be 'Clean' or 'Dirty'. Please try again.")


def get_sequence_length():
    """Ask how many percepts are in the sequence (1, 2, or 3)."""
    valid = ['1', '2', '3']
    while True:
        length = input("\nHow many percepts in the sequence? (1 / 2 / 3): ").strip()
        if length in valid:
            return int(length)
        print(f"  ❌ Invalid input '{length}'. Please enter 1, 2, or 3.")
        
def main():
    print("=" * 55)
    print("       TASK 1 – Table-Driven Agent")
    print("=" * 55)

    length = get_sequence_length()

    percepts = []
    for i in range(length):
        print(f"\n  Percept #{i + 1}:")
        loc    = get_location_input()
        status = get_status_input(loc)
        percepts.append((loc, status))

    if length == 1:
        key = percepts[0]
    else:
        key = tuple(percepts)

    action = table_driven_agent(key)

    print("\n" + "-" * 55)
    print(f"  Percept  : {key}")
    print(f"  Action   : {action}")
    print("-" * 55)

main()