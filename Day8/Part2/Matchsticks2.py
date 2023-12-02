# Function to calculate the total number of characters of string code
def total_character_in_string(data):
    return sum(len(line) for line in data.split("\n"))


# Function to calculate the total number of characters in newly encoded strings
def total_newly_encoded_string(data):
    total = 0
    mylist = data.split("\n")
    for line in mylist:
        total += 2  # Add 2 for the surrounding double quotes
        for i in range(len(line)):
            if line[i] == '"':
                total += 2
            elif line[i] == "\\":
                total += 2
            else:
                total += 1
    return total


def Main():
    file_path = "D:/Adventofcode/2015/Day8/input.txt"
    with open(file_path, "r") as file:
        input = file.read()

    print(
        "The total number of characters of string code minus the total number of characters in memory for string values is: {}".format(
            total_newly_encoded_string(input) - total_character_in_string(input)
        )
    )


if __name__ == "__main__":
    Main()
