import time
import random
import itertools
from boxingascii import frames

# <-----------------------------------------SETTINGS----------------------------------------------------------------->
combo_chance = 0.2
punch_chance = 0.4
reg_interval = 0.7
combo_interval = 0.7
contact_delay = 0.7
starting_delay = 15

rel_punch_freq = [(1, 10), (2, 3), (3, 4), ("OH", 3)]
combos = [(1, 2, 3), (1, 2), (1, 1, 2), (1, 2, "OH", 3), (1, "OH"), (2, 3), (1, 2, 5), (1, 2, "OH", 6)]
# <------------------------------------------------------------------------------------------------------------------>

rel_freq_sum = sum([rel_freq for punch, rel_freq in rel_punch_freq])
punch_selection = list(itertools.chain.from_iterable([[punch for i in range(freq)] for punch, freq in rel_punch_freq]))


def show_punch(punch, interval):
    for frame in frames[str(punch)]:
        print(frame)
        time.sleep(contact_delay / len(frames[str(punch)]))

print("BOXING SIMULATION\n")
print("<--------PUNCH NUMBERS-------->\n1=Jab\n2=Cross\n3=Lead Hook\n5=Lead Uppercut\n6=Rear Uppercut\nOH=Overhand Right\n<---------------------------->\n")
print(f"<--------SETTINGS INFO-------->\nInterval/Combo Interval: {str(reg_interval)}s, {str(combo_interval)}s")
print(f"Punch/Combo Chance: {str(punch_chance * 100)}%, {str(combo_chance * 100)}%\nContact Delay: {str(contact_delay)}s\n<---------------------------->\n")
print(f"<-RELATIVE PUNCH FREQUENCIES AND COMBOS->")
print("Current Combos:")
for combo in combos:
    print(combo)
print("Relative Punch Frequencies:")
for pair in rel_punch_freq:
    print(f"{pair[0]} : {pair[1]/rel_freq_sum*100}%")
print("<--------------------------------------->\n")
input("Press Enter to begin.")
print("Simulation will start in...")
for i in range(starting_delay):
    print(f"{starting_delay-i}...")
    time.sleep(1)

while True:
    if random.random() > (1-combo_chance):
        for punch in random.choice(combos):
            show_punch(punch, combo_interval)
    elif random.random() > (1-punch_chance):
        show_punch(random.choice(punch_selection), reg_interval)
    else:
        for frame in frames["resting"]:
            print(frame)
            time.sleep(reg_interval/len(frames["resting"]))
