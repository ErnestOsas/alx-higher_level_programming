#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print(f"{argc} argument{'s' if argc != 1 else ''}{':' if argc else '.'}")
    print("\n".join(f"{i}: {arg}" for i, arg in enumerate(sys.argv[1:], start=1)))

