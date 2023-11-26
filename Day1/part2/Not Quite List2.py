#Advent of code day1 part2

def basementPosition(input):
    floor = 0
    position = 1

    for i in input:
        if i == "(":
            floor += 1
        if i == ")":
            floor -= 1
            if floor == -1:
                break
        position += 1
    return position


file_path = "input.txt"
with open(file_path, "r") as file:
    file_content = file.read()
print(
    "Santa will reach basement at position: {}".format(basementPosition(file_content))
)
