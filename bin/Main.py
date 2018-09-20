from bin.Compressor import Compressor
from sys import exit

c = Compressor()

# Run until user exits program
while True:
    choice = input("Please enter one of the following options:\n(1) Compress string\n(2) Decompress string\n(3) Exit\n")

    if choice is "1":
        c.compress()
    elif choice is "2":
        c.decompress()
    elif choice is "3":
        print("Exiting PyCompressor...")
        exit()
    else:
        print("That is not a valid option.")