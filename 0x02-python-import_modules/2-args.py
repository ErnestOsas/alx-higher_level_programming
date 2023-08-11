#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args = sys.argv[1:] # exclude the script name
    count = len(args)
    print(f"{count} argument{'s' if count != 1 else ''}.") # use f-string and conditional expression
    for i, arg in enumerate(args, 1): # use enumerate to get index and value
        print(f"{i}: {arg}") # use f-string
