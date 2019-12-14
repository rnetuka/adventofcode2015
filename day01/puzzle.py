directions = {
    '(':  1,
    ')': -1
}


def read_instructions():
    with open('day01/input.txt', 'r') as file:
        instructions = []

        for char in file.readlines()[0]:
            instructions.append(directions[char])

        return instructions


def calculate_floor():
    instructions = read_instructions()
    return sum(instructions)


def basement_index():
    floor = 0
    i = 0

    for instruction in read_instructions():
        floor += instruction
        i += 1
        if floor == -1:
            return i
