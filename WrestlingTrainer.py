import time
import random
import itertools

#<-----------------SETTINGS--------------->
starting_delay = 5
time_multiplier = 1
defense_chance = 0.3
CT_chance = 0.5
collar_tie_delay_range = (0.3, 2)
knee_drop_chance = 1
knee_drop_delay_range = (0.5, 2.5)
#<---------------------------------------->

defense_actions = [("Sprawl", 2), ("Shoot, Sit-Out", 4), ("Shoot, Granby", 3)]
CT_actions = [("Blast Double", 3), ("Push, Fake, Snap, Double", 5), ("Inside Ties, Double", 4), ("Underhook", 2)]
knee_drop_actions = [("Slide by, Double", 4), ("Low Single", 3), ("Low Single, Backdoor, Double", 6), ("Blast Double", 3)]
underhook_actions = [("Shuck, Reverse Tai-O", 4), ("Shuck, Turtle Break, Double", 6), ("High-C, Double", 3)]

def action(action_tuple):
    print(action_tuple[0])
    time.sleep(action_tuple[1] * time_multiplier)
    return action_tuple[0]

input("Press Enter to start.")
print("\nBEGINNING WORKOUT\n")
for i in range(starting_delay):
    print(f"{starting_delay-i}...")
    time.sleep(1)
while True:
    if random.random() > (1-defense_chance):
        action(random.choice(defense_actions))
    elif random.random() > (1-CT_chance):
        print("Collar tie")
        time.sleep(random.uniform(collar_tie_delay_range[0], collar_tie_delay_range[1]))
        if action(random.choice(CT_actions)) == "Underhook":
            action(random.choice(underhook_actions))
    elif random.random() > (1-knee_drop_chance):
        print("Knee Drop")
        time.sleep(random.uniform(knee_drop_delay_range[0], knee_drop_delay_range[1]))
        action(random.choice(knee_drop_actions))