strategy_name = "The GrandMaster"
import random

def move(my_history, their_history):
    if len(my_history) == 0:
        pick = "p"
        return pick
    elif len(my_history) == 1:
        pick = "r"
        return pick
    elif their_history == 'rr':
        pick = "r"
        return pick
    else:
        pick = random.choice(["r", "p", "s"])
        return pick