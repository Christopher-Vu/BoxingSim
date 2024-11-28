import time
import random
import itertools

#<--------------Boxing Settings----------------->
combo_chance = 0.3
punch_chance = 0.3
movement_chance = 1
boxing_interval = 2
combo_interval = 3
punch_interval = 1
inside_movement_interval = 2
#<-------------Kicking Settings----------------->
kick_chance = 0.4
movement_chance = 1
kicking_interval = 1
kick_interval = 2
outside_movement_interval = 2
#<-------------Switch Settings------------------>
boxing_to_kicking_chance = 0.2
kicking_to_boxing_chance = 0.1
range_interval = 1.2
#<--------------Other--------------------------->
starting_delay = 5


rel_punch_freq = [(1, 10), ("Body Jab", 10)]
punch_selection = list(itertools.chain.from_iterable([[punch for i in range(freq)] for punch, freq in rel_punch_freq]))

inside_movements = ["Pull, Drop Step", "L-Step", "Reverse-L Step", "Pivot"]

Combos = ["1-Pull-3", "9-3", "Pull-2-3", "Slip-6-3"]

kicks = ["Teep", "Thigh Teep", "Roundhouse", "Switch Kick", "Fake teep, Roundhouse", "Fake teep, Switch"]
outside_movement = ["Drop Step", "Circle Right", "Circle Left", "L-Step", "Reverse L-Step"]

print("\nBEGINNING WORKOUT\n")
for i in range(starting_delay):
    print(f"{starting_delay-i}...")
    time.sleep(1)
current_range = "kicking"
while True:
    if current_range == "boxing":
        if random.random() > (1-boxing_to_kicking_chance):
            current_range = "kicking"
            print("Back up to kicking range")
            time.sleep(range_interval)
        elif random.random() > (1-combo_chance):
            print(random.choice(Combos))
            time.sleep(combo_interval)
        elif random.random() > (1-punch_chance):
            print(random.choice(punch_selection))
            time.sleep(punch_interval)
        elif random.random() > (1-movement_chance):
            print(random.choice(inside_movements))
            time.sleep(inside_movement_interval)
        else:
            time.sleep(boxing_interval)
    if current_range == "kicking":
        if random.random() > (1-kicking_to_boxing_chance):
            current_range = "boxing"
            print("Close in to boxing range")
            time.sleep(range_interval)
        elif random.random() > (1-kick_chance):
            print(random.choice(kicks))
            time.sleep(kick_interval)
        elif random.random() > (1-movement_chance):
            print(random.choice(outside_movement))
            time.sleep(outside_movement_interval)
        else:
            time.sleep(kicking_interval)
