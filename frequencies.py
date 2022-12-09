"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies_dict = {}
    for item in items:
        frequencies_dict[str(item)] = frequencies_dict.get(str(item), 0) + 1
    return frequencies_dict
