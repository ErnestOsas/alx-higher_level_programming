def print_arguments(argv):
    """Print the number of and list of arguments."""
    count = len(argv)
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print(argv[0])
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, argv[i]))


if __name__ == "__main__":
    argv = sys.argv
    print_arguments(argv)
