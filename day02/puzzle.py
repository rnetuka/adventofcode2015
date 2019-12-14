from collections import namedtuple

Box = namedtuple('Box', 'length, width, height')


def parse_box(string):
    dimensions = string.rstrip().split('x')
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    return Box(length, width, height)


def read_boxes():
    with open('day02/input.txt', 'r') as file:
        boxes = []

        for line in file.readlines():
            boxes.append(parse_box(line))

        return boxes


def wrapping_paper_square_feet():
    result = 0

    for box in read_boxes():
        a = box.length * box.width
        b = box.width * box.height
        c = box.height * box.length
        result += 2*a + 2*b + 2*c + min(a, b, c)

    return result


def ribbon_length(box):
    dimensions = sorted([box.length, box.width, box.height])
    length = 2 * dimensions[0]
    length += 2 * dimensions[1]
    length += box.length * box.width * box.height
    return length


def total_ribbon_length():
    length = 0

    for box in read_boxes():
        length += ribbon_length(box)

    return length
