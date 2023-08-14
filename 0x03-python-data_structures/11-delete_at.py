#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if 0 <= idx < len(my_list):
        my_list.pop(idx)
    return (my_list)
