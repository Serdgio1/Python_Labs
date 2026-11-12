import os
import time

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

def draw_flag():
    radius = 3

    for y in range(-radius * 2, radius * 2 + 1):
        for x in range(-radius * 4, radius * 4 + 1):
            if x**2 + y**2 <= radius**2:
                print(RED + "  " + END, end="")
            else:
                print(WHITE + "  " + END, end="")
        print()

def draw_pattern():
    radius = 5

    for y in range(-radius, radius + 1):
        for x in range(-radius * 2, radius * 2 + 1):

            d1 = abs(x + radius) + abs(y)
            d2 = abs(x - radius) + abs(y)

            if radius - 1 <= d1 <= radius or radius - 1 <= d2 <= radius :
                print("**", end="")
            else:
                print("  ", end="")

        print()

def animate():
    os.system("clear")

    frames = [
        "O",
        "  O",
        "    O",
        "      O",
    ]

    for frame in frames:
        print("\033[H", end="")
        print(frame)
        time.sleep(0.5)
        os.system("clear")

def draw_diagram():
    with open("sequence.txt", "r" ) as file:
        numbers = [float(x) for x in file.readlines()]

    first_group = 0
    second_group = 0

    for number in numbers:
        if number > -5 and number <= 0:
            first_group += 1
        elif number < -5:
            second_group += 1

    total = first_group + second_group

    if total == 0:
        print("We dont have any numbers in the range")
        return

    p1 = (first_group / total) * 100
    p2 = (second_group / total) * 100

    print(f"{BLUE}{" " * round(p1 / 2)}{END} {p1:.2f}%")
    print(f"{RED}{" " * round(p2 / 2)}{END} {p2:.2f}%")

def draw_function():
    width = 30
    height = 10

    graph = [[" " for _ in range(width)] for _ in range(height)]

    for x in range(width):
        graph[height - 1][x] = "-"

    for y in range(height):
        graph[y][0] = "|"

    graph[height - 1][0] = "+"

    for x in range(width):
        y = 3 * x

        screen_y = height - 1 - y // 3

        if 0 <= screen_y < height:
            graph[screen_y][x] = "*"

    print("\n".join("".join(row) for row in graph))

def main():
    draw_flag()
    draw_pattern()
    animate()
    draw_diagram()
    draw_function()

if __name__ == "__main__":
    main()