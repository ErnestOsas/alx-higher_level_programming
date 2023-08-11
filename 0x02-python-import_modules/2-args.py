#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args = sys.argv[1:]
    count = len(args)
    print(f"{count} argument{'s' if count != 1 else ''}.")
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")
