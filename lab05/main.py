def apply_n_times(func, n, value):
    for _ in range(n):
        value = func(value)
    return value

def filter_changed(seq, func, n):
    for item in seq:
        new_item = apply_n_times(func, n, item)
        #if abs(new_item - item) > threshold * abs(item):
        yield new_item

def square(x):
    return x ** 2

numbers = [5, 3, 4, 1, 2]
n = 2

result_generator = filter_changed(numbers, square, n)

out_filter = filter(lambda x: x > 15, result_generator)

sorted_result = list(out_filter)

print(sorted_result)
