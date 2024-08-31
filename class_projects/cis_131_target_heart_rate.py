#cis_131_target_heart_rate.py
'''
script: cis_131_target_heart_rate.py
action: Calculates and displays the user's various heart rate parameters
author: Dylan McCallum
date: 31AUG24

'''

# declare variables

age = int(input("How old are you? "))
max_heart_rate = 0
target_heart_rate_50 = 0
target_heart_rate_85 = 0

# calculations for max heart rate

max_heart_rate = (220 - age)

# calculations for target heart rate zones at 50% and 85%

target_heart_rate_50 = (max_heart_rate * .5)
target_heart_rate_85 = (max_heart_rate * .85)

# display user's heart rates

print(f"\nYour age predicted max heart rate is at " 
      f"{max_heart_rate} bpm at {age} years old according to AHA.")

print(f"\nAt {age} years old, your target HR Zone at 50-85% should be "
      f"between {target_heart_rate_50:.0f}-{target_heart_rate_85:.0f} bpm.")