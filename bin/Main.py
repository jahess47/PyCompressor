from bin.Compressor import Compressor
from sys import exit

c = Compressor()

# Run until user exits program
while True:
    # Get input from user
    choice = input("Please enter one of the following options:\n"
                   "(1) Compress string\n"
                   "(2) Decompress string\n"
                   "(3) Exit\n")

    # Call the Compressor class based on the user's input
    if choice is "1":
        c.compress()
    elif choice is "2":
        c.decompress()
    elif choice is "3":
        print("Exiting PyCompressor...")
        exit()
    else:
        # Catch any input that doesn't match 1, 2, or 3
        print("That is not a valid option.")