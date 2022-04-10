"""
THIS IS NOT MY CODE. ALL CREDIT GOES TO THE AUTHOR OF THE ARTICLE BELOW.

Solving Wordle puzzles with Python.
See https://mathspp.com/blog/solving-wordle-with-python for an article on this.
"""

import collections
import enum


class Tip(enum.Enum):
    ABSENT = 0
    PRESENT = 1
    CORRECT = 2


def score(secret, guess):
    """Scores a guess word when compared to a secret word.
    Makes sure that characters aren't over-counted when they are correct.
    For example, a careless implementation would flag the first “s”
    of “swiss” as PRESENT if the secret word were “chess”.
    However, the first “s” must be flagged as ABSENT.
    To account for this, we start by computing a pool of all the relevant characters
    and then make sure to remove them as they get used.
    """

    # All characters that are not correct go into the usable pool.
    pool = collections.Counter(s for s, g in zip(secret, guess) if s != g)
    # Create a first tentative score by comparing char by char.
    score = []
    for secret_char, guess_char in zip(secret, guess):
        if secret_char == guess_char:
            score.append(Tip.CORRECT)
        elif guess_char in secret and pool[guess_char] > 0:
            score.append(Tip.PRESENT)
            pool[guess_char] -= 1
        else:
            score.append(Tip.ABSENT)

    return score


def filter_words(words, guess, score):
    """Filter words to only keep those that respect the score for the given guess."""

    new_words = []
    for word in words:
        # The pool of characters that account for the PRESENT ones is all the characters
        # that do not correspond to CORRECT positions.
        pool = collections.Counter(c for c, sc in zip(word, score) if sc != Tip.CORRECT)
        for char_w, char_g, sc in zip(word, guess, score):
            if sc == Tip.CORRECT and char_w != char_g:
                break  # Word doesn't have the CORRECT character.
            elif char_w == char_g and sc != Tip.CORRECT:
                break  # If the guess isn't CORRECT, no point in having equal chars.
            elif sc == Tip.PRESENT:
                if not pool[char_g]:
                    break  # Word doesn't have this PRESENT character.
                pool[char_g] -= 1
            elif sc == Tip.ABSENT and pool[char_g]:
                break  # ABSENT character shouldn't be here.
        else:
            new_words.append(word)  # No `break` was hit, so store the word.

    return new_words