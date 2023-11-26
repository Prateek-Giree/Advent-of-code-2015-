# Advent of code 2015 Day1 part1
# ( = one floor up
# ) = one floor down


def countFloor(input):
    floor = 0
    for i in input:
        if i == "(":
            floor += 1
        if i == ")":
            floor -= 1
    return floor


file_path = "input.txt"
with open(file_path, "r") as file:
    file_content = file.read()
print("Santa will reach floor {}".format(countFloor(file_content)))
