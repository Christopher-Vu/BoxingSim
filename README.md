#Boxing Simulator
<hr>
## Summary
Run ASCIIBoxingSim.py for the visual boxing simulator (where an ascii character throws randomized punches at you based on your settings). Run numBasedBoxingSim.py if you just want the numbers and not the full visual.
The character runs on a period system, where during each period, one action can be taken (1 punch). More on that below.
The only punches supported right now are the jab (1), cross (2), lead hook (3), lead and rear uppercuts (5 & 6), and the overhand right (OH).
Each punch (for the ASCII simulator) comprises of three frames stored in a dictionary in boxingascii.py.
<hr>
## Variables / Settings
Settings are changed within the program. You should get all of your settings confirmed through the terminal before beginning the simulation. Here is what you can change:
- combos: this iterable contains all of the possible combos for the character, where each combo is a tuple. 
- rel_punch_freq: the relative frequencies (probability) that a given punch will be thrown, given that a punch will be thrown
- combo_chance: the probability that a combo is initiated during any given period
- punch_chance: the probability that a punch is initiated during any given period, given that a combo was not initiated
- reg_interval: the length of a period
- combo_interval: the length of a period during a combo (you might want this to be faster than a regular period for realism)
- contact_delay: the time between the initiation of a punch and the final frame of that punch
- starting_delay: delay time before starting simulation
