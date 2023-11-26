# It calculates the surface area of each present based on the provided dimensions.
def calculate_surface_area(l, w, h):
    return 2 * (l * w + w * h + h * l) + l * w


def parse_input(input_str):
    # processes the input string to extract the dimensions of each present as a list of lists
    # each inner list contains three sorted integers representing length, width, and height for that present
    return [sorted(map(int, line.split("x"))) for line in input_str.strip().split("\n")]


def total_area(input_str):
    dimensions = parse_input(input_str)
    Required_area = 0
    # store three values from the list(dimensions) in l,w,h respectively and call calculate_surface_area()
    for l, w, h in dimensions:
        Required_area += calculate_surface_area(l, w, h)
    return Required_area


file_path = "input.txt"
with open(file_path, "r") as file:
    input_data = file.read()

print(
    "The elves should order {} square feets of wrapping papers".format(
        +total_area(input_data)
    )
)
