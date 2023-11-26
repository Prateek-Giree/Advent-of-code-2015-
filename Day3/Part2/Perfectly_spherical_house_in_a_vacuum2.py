def count_unique_house(direction):
    visited_houses = {(0, 0)}

    x, y = 0, 0  # position of santa
    X, Y = 0, 0  # position of robo santa

    # santa moves the even index
    for pos in range(0, len(direction), 2):
        if direction[pos] == ">":
            x += 1
        elif direction[pos] == "<":
            x -= 1
        elif direction[pos] == "^":
            y += 1
        elif direction[pos] == "v":
            y -= 1

        visited_houses.add((x, y))

    # robo santa moves the odd index
    for POS in range(1, len(direction), 2):
        if direction[POS] == ">":
            X += 1
        elif direction[POS] == "<":
            X -= 1
        elif direction[POS] == "^":
            Y += 1
        elif direction[POS] == "v":
            Y -= 1

        visited_houses.add((X, Y))

    # There are two (0,0) so in list so removing 1
    return len(visited_houses)


with open("f:2015\\Day3\\input.txt", "r") as file:
    puzzle_input = file.read()
input_data = list(puzzle_input)

print(
    "Number of houses that receive at least one present are: {}".format(
        count_unique_house(input_data)
    )
)
