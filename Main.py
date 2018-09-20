import Compressor
from sys import exit

c = Compressor()

choice = input("Please enter one of the following options:\n(1) Compress string\n(2) Decompress string\n(3) Exit")

# Run until user exits program
while True:
    if choice is 1:
        c.compress()
    elif choice is 2:
        c.decompress()
    elif choice is 3:
        exit()
    else:
        print("That is not a valid option.")