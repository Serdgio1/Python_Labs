class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


def knapsack(items, capacity):
    dp = [(0, ()) for _ in range(capacity + 1)]

    for i, item in enumerate(items):
        for w in range(capacity, item.weight - 1, -1):
            previous_value, previous_item = dp[w - item.weight]

            new_value = previous_value + item.value

            if new_value > dp[w][0]:
                dp[w] = (new_value, previous_item + (i, ))

    best_value, selected_items = max(dp, key=lambda item: item[0])

    selected = [items[i] for i in selected_items]

    return selected, best_value

def find_all_solutions(items, capacity, initial_points):
    solutions = []
    n = len(items)

    for mask in range(1 << n):
        selected = []

        for i in range(n):
            if mask & (1 << i):
                selected.append(items[i])

        used_space = sum(item.weight for item in selected)

        if used_space > capacity:
            continue

        score = calculate_score(items, selected, initial_points)

        if score > 0:
            solutions.append((selected, used_space, score))

    return solutions


def calculate_score(items, selected, initial_points):
    taken_value = sum(item.value for item in selected)
    total_value = sum(item.value for item in items)
    left_value = total_value - taken_value

    return initial_points + taken_value - left_value



def print_inventory(selected, rows, cols):
    inventory = [[' '] * cols for _ in range(rows)]

    position = 0

    for item in selected:
        for _ in range(item.weight):
            row = position // cols
            col = position % cols

            inventory[row][col] = item.name
            position += 1

    for row in inventory:
        print(', '.join(f'[{cell}]' for cell in row))


if __name__ == '__main__':
    items = [
        Item('r', 3, 25),
        Item('p', 2, 15),
        Item('a', 2, 15),
        Item('m', 2, 20),
        Item('i', 1, 5),
        Item('k', 1, 15),
        Item('x', 3, 20),
        Item('t', 1, 25),
        Item('f', 1, 15),
        Item('d', 1, 10),
        Item('s', 2, 20),
        Item('c', 2, 20)
    ]

    rows = 2
    cols = 4
    capacity = rows * cols
    initial_points = 15

    selected, value = knapsack(items, capacity)

    score = calculate_score(items, selected, initial_points)

    print("Inventory:")
    print_inventory(selected, rows, cols)
    print("points:", score)

    print("additional task")

    solutions = find_all_solutions(items, 7, initial_points)

    if solutions:
        print("Solution found: ", len(solutions))

        for selected, used_space, score in solutions:
            names = ''.join(item.name for item in selected)
            print(names, "Cells: ", used_space, "Points: ", score)
    else:
        print("No solution found")

    print("additional task 2")

    solutions = find_all_solutions(items, capacity, initial_points)

    print("Solution found: ", len(solutions))

    for selected, used_space, score in solutions:
        names = ''.join(item.name for item in selected)
        print(names, "Cells: ", used_space, "Points: ", score)