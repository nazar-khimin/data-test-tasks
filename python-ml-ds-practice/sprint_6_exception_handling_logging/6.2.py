import cmath

def solve_quadric_equation(a: float, b: float, c: float):
    try:
        if a == 0:
            return "Zero Division Error"

        discriminant = b ** 2 - 4 * a * c

        x1 = (-b - cmath.sqrt(discriminant)) / 2 * a
        x2 = (-b + cmath.sqrt(discriminant)) / 2 * a
        return f'The solution are x1={x1} and x2={x2}'

    except TypeError:
        return "Could not convert string to float"


print(solve_quadric_equation(1, 3, -4))
