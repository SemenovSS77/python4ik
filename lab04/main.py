def check_args(f):
    def wrapper(*args):
        if any(not isinstance(arg, (int, float)) or not (0 <= arg <= 100) for arg in args):
            raise ValueError("Ошибка")
        return f(*args)
    return wrapper

@check_args
def calculate_average(*args):
    return sum(args) / len(args) if args else 0

try:
    print(calculate_average(10, 20, 30, 100))
except ValueError as error:
    print(error)