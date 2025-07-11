def calc(a, b, op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b
    raise ValueError("Incorrect operation is obtained")


def run_calc(a, b, op):
    try:
        print(calc(a, b, op))
    except ZeroDivisionError:
        print("Division by zero")
    except TypeError:
        print("TypeError")
    except ValueError as e:
        print(e)

    print("End of calculation")


run_calc(8, 2, 4)

