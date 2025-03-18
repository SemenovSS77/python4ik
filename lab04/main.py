def validate_args(ex_type, min_v, max_v):
    def decorator(f):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, ex_type):
                    raise ValueError(f"Ошибка. Аргумент {arg} должен быть типа {ex_type}")
                if not (min_v <= arg <= max_v):
                    raise ValueError(f"Ошибка. Аргумент {arg} должен быть в диапозоне от {min_v} до {max_v}")
            return f(*args, **kwargs)
        return wrapper
    return decorator

def average():
    total = 0
    count = 0
    
    @validate_args(int, 1, 100)
    def add_number(num):
        nonlocal total, count
        total += num
        count += 1
        return total / count
    return add_number

avg = average()

print(avg(5.5))
print(avg(9))
print(avg(15))
print(avg(100))
