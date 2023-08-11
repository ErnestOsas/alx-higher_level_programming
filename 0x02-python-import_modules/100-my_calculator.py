import sys
from calculator import add, sub, mul, div

def main():
    """Calculates the result of an arithmetic expression."""
    if len(sys.argv) != 4:
        print("Usage: python3 calculator.py <a> <operator> <b>")
        sys.exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
    except ValueError:
        print("Invalid number.")
        sys.exit(1)

    operator = sys.argv[2]
    if operator not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    func = {"+": add, "-" : sub, "*": mul, "/" : div}[operator]
    result = func(a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))

if __name__ == "__main__":
    main()
