import random
import pyjokes

reactions = [
    "Hilarious!",
    "Oh, the humanity!",
    "You've cracked the code!",
    "That's comedy gold!",
    "My sides are splitting!",
    "Mind = blown!",
    "Cue the laugh track!",
    "I'm dying of laughter!",
    "That's so bad, it's good!",
    "*Insert uncontrollable laughter here*",
]


def get_random_reaction():
    return random.choice(reactions)


def print_random_joke_and_reaction():
    print(f"Joke: {pyjokes.get_joke()}\nReaction: {get_random_reaction()}")


if __name__ == "__main__":
    print_random_joke_and_reaction()
