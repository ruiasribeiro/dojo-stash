from dataclasses import dataclass
from enum import Enum

Character = Enum("Character", "GHOST HUMAN ZOMBIE")


@dataclass
class Answer:
    text: str
    value: Character


@dataclass
class Question:
    text: str
    answers: list[Answer]


QUESTIONS = [
    Question(
        "Is Halloween scary for you?",
        [
            Answer("Yeah! Too much...", Character.HUMAN),
            Answer("Meh.", Character.GHOST),
            Answer("Of course not, I'm the one scaring others.", Character.ZOMBIE),
        ],
    ),
    Question(
        "Trick or treat?",
        [
            Answer("Trick!", Character.GHOST),
            Answer("Treat!", Character.ZOMBIE),
            Answer("What? I don't even like Halloween...", Character.HUMAN),
        ],
    ),
]


def main():
    print("Welcome to the Halloween quiz!\nWe'll try to guess which monster you are.")

    # Create a map with all possible results zeroed out.
    choices = dict.fromkeys(Character, 0)

    # Loop through all the questions while collecting the answers.
    for (i, question) in enumerate(QUESTIONS):
        print(f"\nQuestion {i+1}: {question.text}")

        for (j, answer) in enumerate(question.answers):
            print(f"{j+1}: {answer.text}")

        choice = input("\nChoose an answer: ")
        while isinstance(choice, str):
            try:
                choice = int(choice) - 1

                if choice < 0 or choice >= len(question.answers):
                    raise IndexError

                answer = question.answers[choice]
                choices[answer.value] += 1
            except (ValueError, IndexError):
                choice = input("Invalid number! Please try again: ")

    # Calculate the resulting character.
    result = max(choices, key=lambda key: choices[key])
    print("\nResult:")
    match result:
        case Character.GHOST:
            print("You're a ghost! Booo 👻")
        case Character.HUMAN:
            print("You're a human?! 😱\nOnly monsters are allowed in Halloween!")
        case Character.ZOMBIE:
            print("You're a zombie... Brainzzz... 🧟")


if __name__ == "__main__":
    main()
