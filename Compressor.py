class Compressor:

    # Initializer
    def __init__(self):
        print("Welcome to PyCompressor!")

    # Compress the given string
    def compress(self):
        string = input("Please enter string to be compressed: ")

        count = 0
        initial_value = input[0]
        new_string = ""

        # Example:
        # "aabbbccb"
        #  01234567
        for i in range(0, len(string)):
            if string[i] is initial_value:
                count += 1
            else:
                new_string += str(count) + str(initial_value)
                count = 1
                initial_value = string[i]

        print("Newly compressed string: " + new_string)

    # Decompress the given string
    def decompress(self):
        string = input("Please enter the string to be decompressed: ")

        count = 0
        new_string = ""

        for i in range(0, len(string)):
            if string.isnumeric():
                count += 1
            else:
                for j in range(0, int(string[i-count:i])):
                    new_string += string[i]

                count = 0