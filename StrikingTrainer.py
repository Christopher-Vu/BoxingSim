import time
import random
import itertools

combo_chance = 0.3
punch_chance = 0.3
movement_chance = 1
boxing_interval = 2
combo_interval = 3
punch_interval = 1
movement_interval = 2

rel_punch_freq = [(1, 10), (2, 3), (3, 4), ("OH", 3)]
punch_selection = list(itertools.chain.from_iterable([[punch for i in range(freq)] for punch, freq in rel_punch_freq]))

boxing_movements = ["Pull, Drop Step", "L-Step", "Reverse-L Step", "Pivot"]

Combos = ["1-Pull-3", "9-3", "Pull-2-3", "Slip-6-3"]

print("\nBEGINNING WORKOUT\n")
print("<---------------->\n1=Jab\n2=Cross\n3=Lead Hook\n6=Rear Uppercut\n<---------------->\n")
while True:
    if random.random() > (1-combo_chance):
        print(random.choice(Combos))
        time.sleep(combo_interval)
    elif random.random() > (1-punch_chance):
        print(random.choice(punch_selection))
        time.sleep(punch_interval)
    elif random.random() > (1-movement_chance):
        print(random.choice(boxing_movements))
        time.sleep(movement_interval)
    else:
        time.sleep(boxing_interval)
