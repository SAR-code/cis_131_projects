'''
script: class_notes_29.py  
action: runs class notes for the week of 29th oct
author: Dylan McCallum
date: 29OCT24
'''

'''
Tower of hanoi

n disks

    (n-1) disks to temp spot
    move n to target
    move n-1 to target
    
    
    def h_tower(num, source, target):
    
project info

key data structures

Class person
    
'''

def h_tower(num, source, target, aux):
    
    if(num == 1):
        print (f"Move disk 1 from source {source} to target {target}")
        
        return h_tower(n-1, aux, target, source)
    
    print(f"Move disk {num} from source, {source} to target {target}")
    h_tower(n-1, aux, target, source)
    

n = 2
print(h_tower(n,'A','B','C'))
    