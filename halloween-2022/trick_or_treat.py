# Loosely based on the great 'The Evolution of Trust', by Nicky Case.
# https://ncase.me/trust/


from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable


# =====================================
# Data structures
# =====================================


class Move(Enum):
    TRICK = auto()
    TREAT = auto()

    def spent(self) -> int:
        """
        Calculates how many points a player has spent in a given play,
        according to the move they made.
        """

        match self:
            case Move.TRICK:
                return 0
            case Move.TREAT:
                return 1

    def gained(self) -> int:
        """
        Calculates how many points a player has gained in a given play,
        according to the move their opponent made.
        """

        match self:
            case Move.TRICK:
                return 0
            case Move.TREAT:
                return 3


@dataclass
class Play:
    by_player: Move
    by_opponent: Move


@dataclass
class Opponent:
    strategy: Callable[[Play | None], Move]

    def play(self, last_play: Play | None) -> Move:
        return self.strategy(last_play)


# =====================================
# Opponent strategies
# =====================================


def copycat_strategy(last_play: Play | None) -> Move:
    """Copies the last move of the player, starting with a treat."""

    match last_play:
        case Play(by_player, _):
            return by_player
        case None:
            return Move.TREAT


def trickster_strategy(_) -> Move:
    """Always plays with a trick."""
    return Move.TRICK


def treater_strategy(_) -> Move:
    """Always plays with a treat."""
    return Move.TREAT


# =====================================
# Game loop
# =====================================


def main() -> None:
    game_loop()


def game_loop() -> None:
    opponent = Opponent(copycat_strategy)
    last_play = None
    scores = (0, 0)

    while True:
        move = input_move()
        op_move = opponent.play(last_play)

        last_play = Play(move, op_move)
        print(f"The play was: {last_play}")

        scores = (
            scores[0] - move.spent() + op_move.gained(),
            scores[1] - op_move.spent() + move.gained(),
        )
        print(f"Current scores: {scores}\n")


def input_move() -> Move:
    move = input("Trick (1) or treat (2)? ")

    while isinstance(move, str):
        try:
            move = int(move)
            match move:
                case 1:
                    move = Move.TRICK
                case 2:
                    move = Move.TREAT
                case _:
                    raise ValueError
        except ValueError:
            move = input("Invalid input! Please try again: ")

    return move


if __name__ == "__main__":
    main()
