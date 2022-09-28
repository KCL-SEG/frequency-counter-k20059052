"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
 
    frequencies = {}
    if len(items) != 0:
        
    
        
        frequencies[str(items[0])] = 0
        
    for item in items:
        item = str(item)
        if item in frequencies.keys():
            frequencies[item] += 1
            
        else:
            frequencies[item] = 1
    print(frequencies)
    
    return frequencies
items = ['a', 'a', 'b', 'b', 'b', 'c']   
frequencies(items)

def frequencies(items):
    frequencies = {}
    # Your code goes here
    return frequencies
