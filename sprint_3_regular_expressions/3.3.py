import math


def extract_coordinates(s):
    points = {}
    segments = s.split('#')

    for segment in segments:
        if segment:
            point, coords = segment[:2], segment[2:]
            x, y = map(int, coords.split(':'))
            points[point] = (x, y)

    return points


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def figure_perimetr(s):
    points = extract_coordinates(s)

    points_order = ['LB', 'RB', 'RT', 'LT']

    perimeter = 0
    for i in range(len(points_order)):
        p1 = points[points_order[i]]
        p2 = points[points_order[(i + 1) % len(points_order)]]  # Next point, wrap around
        perimeter += distance(p1, p2)

    return perimeter


test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))