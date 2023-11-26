def calculate_ribbon_area(l, w, h):
    return 2 * (l + w) + (l * w * h)


def total_ribbon_area(input):
    dimension = parse_input(input)
    required_area = 0
    for l, w, h in dimension:
        required_area += calculate_ribbon_area(l, w, h)
    return required_area


def parse_input(input):
    return [sorted(map(int, line.split("x"))) for line in input.strip().split("\n")]


with open("input.txt", "r") as file:
    input_data = file.read()

print(
    "The elves should order {} square feets  of ribbon ".format(
        total_ribbon_area(input_data)
    )
)
