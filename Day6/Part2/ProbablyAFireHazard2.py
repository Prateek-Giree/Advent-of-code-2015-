def update_grid(grid, inp):
    inp = inp.split()
    if inp[0] == "turn":
        action = inp[1]
        start = list(map(int, inp[2].split(",")))
        end = list(map(int, inp[4].split(",")))

        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                if action == "on":
                    grid[x][y] += 1
                elif action == "off":
                    grid[x][y] = max(0, grid[x][y] - 1)

    else:
        start = list(map(int, inp[1].split(",")))
        end = list(map(int, inp[3].split(",")))

        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                grid[x][y] += 2


def total_brightness(grid):
    # inner sum()calculate the sum of value within single row and outer sum() sums up each row to calculate total brightness
    return sum(sum(row) for row in grid)


with open("input.txt", "r") as file:
    input_data = file.read().splitlines()


grid = [[0] * 1000 for _ in range(1000)]
for i in input_data:
    update_grid(grid, i)

print("The number of lights on are:", total_brightness(grid))
