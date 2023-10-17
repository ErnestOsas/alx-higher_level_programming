#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        kes = fct(*args)
    except BaseException as e:
        kes = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return kes
