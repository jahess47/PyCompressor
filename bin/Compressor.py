class Compressor:

    # Initializer
    def __init__(self):
        print("Welcome to PyCompressor!")

    # Compress the given string
    def compress(self):
        string = input("Please enter string to be compressed: ")

        count = 0                  # Holds the number of indexes the character is the same
        initial_value = string[0]  # Holds the initial character within each "block"
        new_string = ""            # Holds the newly compressed string

        # Iterate through string and populate new_string with the correct values
        for i in range(0, len(string)):
            if string[i] is initial_value:
                count += 1

                if i is len(string) - 1:
                    new_string += str(count) + str(initial_value)
            else:
                new_string += str(count) + str(initial_value)
                initial_value = string[i]

                if i is len(string) - 1:
                    new_string += str(1) + str(initial_value)

                count = 1
                initial_value = string[i]

        print("Newly compressed string: " + new_string)

    # Decompress the given string
    def decompress(self):
        string = input("Please enter the string to be decompressed: ")

        count = 0        # Holds the number of indexes that there's a number
        new_string = ""  # Holds the newly decompressed string

        # Iterate through string and populate new_string with the correct values
        for i in range(0, len(string)):
            if string[i].isnumeric():
                count += 1
            else:
                for j in range(0, int(string[i-count:i])):
                    new_string += string[i]

                count = 0

        print("Newly decompressed string: " + new_string)