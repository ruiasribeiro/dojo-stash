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
    # TODO: grab user input
    # TODO: call generate_pairings() with the input
    # TODO: pretty print the results
    pass


if __name__ == "__main__":
    main()
