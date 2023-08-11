import sys

if __name__ != "__main__":
    exit()

argString = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argString += 's.'
elif argc == 1:
    argString += ':'
else:
    argString += 's:'
print(argString.format(argc))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
