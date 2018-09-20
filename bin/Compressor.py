class Compressor:

    # Initializer
    def __init__(self):
        print("Welcome to PyCompressor!")

    # Compress the given string
    def compress(self):
        string = input("Please enter string to be compressed: ")

        count = 0
        initial_value = string[0]
        new_string = ""

        """
        if (chars[i] == initialChar) {
                indexCount++;

                if (i == chars.length - 1) {
                    newDna += (Integer.toString(indexCount) + Character.toString(initialChar));
                }
            } else {
                newDna += (Integer.toString(indexCount) + Character.toString(initialChar));
                initialChar = chars[i];

                if (i == chars.length - 1) {
                    newDna += (Integer.toString(1) + Character.toString(initialChar));
                }

                indexCount = 1;
            }
        """
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

        count = 0
        new_string = ""

        for i in range(0, len(string)):
            if string[i].isnumeric():
                count += 1
            else:
                for j in range(0, int(string[i-count:i])):
                    new_string += string[i]

                count = 0

        print("Newly decompressed string: " + new_string)