def count_unique_houses(input):
    visited_houses = [
        (0, 0)
    ]  # List to keep track of visited houses. We start at the origin (0, 0).
    x, y = 0, 0  # Santa's current position

    for pos in input:
        if pos == ">":
            x += 1
        elif pos == "<":
            x -= 1
        elif pos == "^":
            y += 1
        elif pos == "v":
            y -= 1

        # Check if the current position is already in the list, and only add if it's not already there
        if (x, y) not in visited_houses:
            visited_houses.append((x, y))

    return visited_houses


with open("input.txt", "r") as file:
    input = file.read()

print(
    "Number of houses visited at least once: {}".format(len(count_unique_houses(input)))
)
