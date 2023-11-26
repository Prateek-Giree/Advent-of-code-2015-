def nice_naughty_string(input_data):
    # to check the presence of vowel
    vowel = set("aeiou")
    vowel_count = 0
    for char in input_data:
        if char in vowel:
            vowel_count += 1
    if vowel_count < 3:
        return False

    # to check at least one letter that appears twice in a row
    if not any(input_data[i] == input_data[i + 1] for i in range(len(input_data) - 1)):
        return False

    # to check is it contain disallowed strings
    disallowed_strings = {"ab", "cd", "pq", "xy"}
    if any(j in input_data for j in disallowed_strings):
        return False
    else:
        return True


with open("input.txt", "r") as file:
    input_data = file.read()

nice_string = 0
input_data = input_data.split("\n")
for i in input_data:
    if nice_naughty_string(i):
        nice_string += 1
print("The number of nice strings are {} ".format(nice_string))