def main():
    face = [
        r"o    o",
        r" ---- ",
    ]

    for line in make_pumpkin(face):
        print(line)


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
