import sys

def print_python_list_info(p):
    """Prints basic info about Python lists."""
    size = len(p)
    alloc = sys.getsizeof(p)

    print(f"[*] Size of the Python List = {size}")
    print(f"[*] Allocated = {alloc}")

    for i, obj in enumerate(p):
        print(f"Element {i}: {type(obj).__name__}")
