import time
import random
import itertools
from boxingascii import frames

combo_chance = 0.1
punch_chance = 0.3
reg_interval = 1
combo_interval = 1
contact_delay = 0.8
starting_delay = 3

rel_punch_freq = [(1, 10), (2, 3), (3, 4), ("OH", 3)]
punch_selection = list(itertools.chain.from_iterable([[punch for i in range(freq)] for punch, freq in rel_punch_freq]))

Combos = [(1, 2, 3), (1, 2), (1, 1, 2), (1, 2, "OH", 3), (1, "OH"), (2, 3), (1, 2, 5), (1, 2, "OH", 6)]

def show_punch(punch, interval):
    for frame in frames[str(punch)]:
        print(frame)
        time.sleep(contact_delay / len(frames[str(punch)]))
    time.sleep(interval-contact_delay)

print("\nBEGINNING SIMULATION\n")
print("<---------------->\n1=Jab\n2=Cross\n3=Lead Hook\n5=Lead Uppercut\n6=Rear Uppercut\nOH=Overhand Right\n<---------------->\n")
print(f"Punch number will show {str(contact_delay)} seconds before landing.\nThe asterisk (*) means the punch conntected.")
input("Press Enter to begin.")
print("Simulation will start in...")
for i in range(starting_delay):
    print(f"{starting_delay-i}...")

while True:
    if random.random() > (1-combo_chance):
        for punch in random.choice(Combos):
            show_punch(punch, combo_interval)
    elif random.random() > (1-punch_chance):
        show_punch(random.choice(punch_selection), reg_interval)
    else:
        for frame in frames["resting"]:
            print(frame)
            time.sleep(reg_interval/len(frames["resting"]))
