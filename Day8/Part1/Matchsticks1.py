# Function to calculate the total number of characters of string code
def total_character_in_string(data):
    return sum(len(line) for line in data.split("\n"))


def total_character_in_memory(data):
    total = 0
    mylist = data.split("\n")
    for line in mylist:
        line = line[1:-1]  # Remove surrounding double quotes
        i = 0
        while i < len(line):
            if line[i] == "\\":
                if line[i + 1] == "\\" or line[i + 1] == '"':
                    i += 1  # Skip the escaped character
                elif line[i + 1] == "x":
                    i += 3  # Skip the hexadecimal characters
            total += 1  # Increment total character count
            i += 1
    return total


def Main():
    file_path = "D:/Adventofcode/2015/Day8/input.txt"
    with open(file_path, "r") as file:
        input = file.read()

    print(
        "The total number of characters of string code minus the total number of characters in memory for string values is: {}".format(
            total_character_in_string(input) - total_character_in_memory(input)
        )
    )


if __name__ == "__main__":
    Main()
