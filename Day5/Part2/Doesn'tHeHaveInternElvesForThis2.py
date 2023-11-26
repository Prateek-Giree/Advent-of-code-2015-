def nice_naughty_string(input_data):
    count = 0

    # at least one letter which repeats with exactly one letter between them
    if not any(
        input_data[character] == input_data[character + 2]
        for character in range(len(input_data) - 2)
    ):
        return False

    #  pair of any two letters that appears at least twice in the string without overlapping
    if not any(
        input_data[character : character + 2] in input_data[character + 2 :]
        for character in range(len(input_data) - 1)
    ):
        return False

    return True


with open("input.txt", "r") as file:
    input_data = file.read()


input_data = input_data.split("\n")
nice_string = 0
for i in input_data:
    if nice_naughty_string(i):
        nice_string += 1
print("The number of nice strings are {} ".format(nice_string))
