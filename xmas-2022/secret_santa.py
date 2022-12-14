import random


def generate_pairings(names: list[str]) -> list[tuple[str, str]]:
    running = True
    pairings = []

    while running:
        receivers = names.copy()

        for giver in names:
            # This ensures that there isn't anyone left at the end without a
            # pairing.
            if len(receivers) == 1:
                if receivers[0] == giver:
                    pairings = []
                    break
                else:
                    running = False

            choice = -1
            while choice == -1 or receivers[choice] == giver:
                choice = random.randint(0, len(receivers) - 1)

            receiver = receivers.pop(choice)
            pairings.append((giver, receiver))

    return pairings


def main():
    print("Welcome to the Secret Santa generator!")
    print("Input an empty name to end.\n")

    names = []
    inputting = True

    while inputting:
        name = input("Insert a name: ")
        if name == "":
            inputting = False
        else:
            names.append(name)

    if len(names) < 2:
        print("\nNot enough names inputted! Specify at least 2.")
        return

    pairings = generate_pairings(names)

    max_name_length = max(map(lambda pair: len(pair[0]), pairings))

    print("\nHere are the results:")
    print(f"{'giver' : >{max_name_length}} --> receiver\n")
    for giver, receiver in pairings:
        print(f"{giver : >{max_name_length}} --> {receiver}")


if __name__ == "__main__":
    main()
