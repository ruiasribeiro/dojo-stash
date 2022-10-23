# A GUI version of `trick_or_treat.py`, needs `guizero` installed.

# Loosely based on the great 'The Evolution of Trust', by Nicky Case.
# https://ncase.me/trust/


from dataclasses import dataclass
from enum import Enum, auto
from typing import Callable

from guizero import App, Box, PushButton, Text


# =====================================
# Data structures
# =====================================


class Move(Enum):
    TRICK = auto()
    TREAT = auto()

    def __str__(self) -> str:
        match self:
            case Move.TRICK:
                return "Trick"
            case Move.TREAT:
                return "Treat"

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

    def __str__(self) -> str:
        return f"Last Play: You ({self.by_player}) vs CPU ({self.by_opponent})"


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
# Game state
# =====================================

opponent = Opponent(copycat_strategy)
last_play = None
round = 1
scores = (0, 0)


def play(move: Move):
    global last_play, opponent, round, scores

    op_move = opponent.play(last_play)

    last_play = Play(move, op_move)

    round += 1
    scores = (
        scores[0] - move.spent() + op_move.gained(),
        scores[1] - op_move.spent() + move.gained(),
    )

    # Update GUI.
    last_play_text.value = f"{last_play}"
    scores_text.value = f"Round {round}, Scores: {scores}"


# =====================================
# GUI initialization
# =====================================

app = App(title="Trick or treat?", width=350, height=150)

Text(app, text="Trick or treat?")
last_play_text = Text(app, text=f"Let's start!")
scores_text = Text(app, text=f"Round {round}")

buttons_box = Box(app, align="bottom")
PushButton(buttons_box, text="Trick", align="left", command=lambda: play(Move.TRICK))
PushButton(buttons_box, text="Treat", align="right", command=lambda: play(Move.TREAT))

app.display()
