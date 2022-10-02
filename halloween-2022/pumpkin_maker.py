EYES = [
    r"V    V",
    r"^    ^",
    r"O    O",
]

NOSES = [
    r"   >  ",
    r"  <   ",
    r"      ",
]

MOUTHS = [
    r" ---- ",
    r" v--v ",
    r" #### ",
]


def main():
    print(
        "Welcome to the Pumpkin Maker! Here you can make the pumpkin of your "
        "dreams (or perhaps your nightmares...)"
    )

    eyes = select("Pick your eyes!", EYES)
    nose = select("Pick your nose!", NOSES)
    mouth = select("Pick your mouth!", MOUTHS)

    print("\n########################\n\nHere's the final result!\n")

    face = [eyes, nose, mouth]
    for line in make_pumpkin(face):
        print(line)


def select(prompt: str, options: list[str]) -> str:
    print(f"\n{prompt}")

    for (i, option) in enumerate(options):
        print(f"{i+1}. {option}", end="\t")

    choice = input("\nChoose an option: ")
    while isinstance(choice, str):
        try:
            choice = int(choice) - 1
            if choice < 0 or choice >= len(options):
                raise IndexError
        except (ValueError, IndexError):
            choice = input("Invalid number! Please choose again: ")

    return options[choice]


def make_pumpkin(face: list[str]) -> list[str]:
    face = [f"|      {line}      |" for line in face]

    return [
        r"          .",
        r"  _  _  _/ _  _  _",
        r" / \/ \/ \/ \/ \/ \ ",
        r"|                  |",
        *face,
        r"|                  |",
        r" \_/\_/\_/\_/\_/\_/ ",
    ]


if __name__ == "__main__":
    main()
