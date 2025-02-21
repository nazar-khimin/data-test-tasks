class MyExceptions(Exception):
    pass


def sum_slice_array(arr, first, second):
    try:
        if not isinstance(first, int) or not isinstance(second, int) or first < 1 or second < 1:
            raise MyExceptions()
        if first > len(arr) or second > len(arr):
            raise MyExceptions()
        val1 = arr[first - 1]
        val2 = arr[second - 1]
        if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
            raise MyExceptions()
        return float(val1 + val2)
    except (TypeError, ValueError):
        raise MyExceptions()

print(sum_slice_array([1, 2, 3], 1, 2))

try:
    print(sum_slice_array([1, "string", 3], 1, 2))
except MyExceptions:
    print("MyExceptions")

try:
    print(sum_slice_array([14, 5, 3], -1, 2))
except MyExceptions:
    print("MyExceptions")