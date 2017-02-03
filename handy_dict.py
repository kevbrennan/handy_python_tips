# -*- coding: utf-8 -*-
"""
Spyder Editor

handy_dict.py
"""

my_dict = {
        'kev': 49,
        'tracey': 51,
        'amy': 15,
        'aidan': 49
        }

# search for all cases of a value in a dictionary(not the key)
def search_dict(val, my_dict):
    # dictionary to hold return values
    result = {}
    
    # check whether value == val and add to dictionary result
    for  the_key, the_value in my_dict.items():
        if the_value == val:
            result[the_key]= the_value
    
    # If result is not empty return it, if not return message               
    if result:
        return result
    else:
        return '{} not found in dictionary'.format(val)                  
        
        