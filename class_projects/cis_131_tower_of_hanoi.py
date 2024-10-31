'''
script: cis_131_towwer_of_hanoi.py
action: Demonstrates the towers of hanoi exercise
author: Dylan McCallum
date: 29OCT24
'''

# declare function to establish the towers

def tower_h(num, source, destination, aux):
    '''
    This function uses recursion to facilitate the movement of towers 
    from one tower to another
    
    action: Demonstrates the Towers of Hanoi problem
    
    input:  The number of disks, the original source, the auxiliary/helper
            tower and the final destination.
    
    output: The movement of the disks onto each of the towers
            without stacking on top of each other
    
    return: None
    
    '''
    
    # if base case
    
    if num == 1:
        print(f"Move 1 disk from source {source}, to destination {destination}")
        return
    
    # displays the movement between disks and destinations
    
    tower_h(num - 1, source, aux, destination)
    print(f"Move disk {num} from source {source} to destination {destination}")
    tower_h(num -1, aux, destination, source)

# store a function into a variable
start_tower = tower_h(3,'A', 'B', 'C')

# display the variable
print(start_tower)