def outer(name):
    def inner():
        print(f"Hello, {name}!")
    return inner


if ('outer' in locals()):
 print('function "outer" is present')
else:
 print('function "outer" is absent')