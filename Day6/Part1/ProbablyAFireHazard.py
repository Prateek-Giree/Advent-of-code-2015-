def update_grid(grid, inp):
    inp = inp.split()
    if inp[0] == "turn":
        action = inp[1]

        # converting string at index 2 (ie x1,y1) into int after splitting at ","
        start = list(map(int, inp[2].split(",")))
        # converting string at index 4 (ie x2,y2)into int after splitting at ","
        end = list(map(int, inp[4].split(",")))

        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if action == "on":
                    grid[x][y] = 1
                elif action == "off":
                    grid[x][y] = 0

    else:
        start = list(map(int, inp[1].split(",")))
        end = list(map(int, inp[3].split(",")))

        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                grid[x][y] = 1 - grid[x][y]


def count_lights_on(grid):
    return sum(row.count(1) for row in grid)


with open("input.txt", "r") as file:
    input_data = file.read().splitlines()


# create of 1000x1000 grid of 0's
grid = [[0] * 1000 for _ in range(1000)]
for i in input_data:
    update_grid(grid, i)

print("The number of lights on are:", count_lights_on(grid))
