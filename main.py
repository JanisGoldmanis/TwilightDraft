import random
from constants import FACTIONS, KELERES_CHILDREN, KELERES


def keleres_check(faction, available_factions, keleres, keleres_children):
    if faction == keleres:
        for child in keleres_children:
            available_factions.remove(child)
    elif faction in keleres_children:
        if keleres in available_factions:
            available_factions.remove(keleres)


seed = 2
random.seed(seed)

drawn_factions = []
factions_to_draw = 8

available_factions = FACTIONS[:]

for _ in range(factions_to_draw):
    index = random.randint(0, len(available_factions) - 1)
    faction = available_factions.pop(index)
    drawn_factions.append(faction)
    keleres_check(faction, available_factions, KELERES, KELERES_CHILDREN)

for i, faction in enumerate(drawn_factions, start=1):
    print(f'{i} | {faction}')
