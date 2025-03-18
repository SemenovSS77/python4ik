# 1) Функция для линеаризации вложенных списков
def linearize_recursive(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return linearize_recursive(lst[0]) + linearize_recursive(lst[1:])
    return [lst[0]] + linearize_recursive(lst[1:])

def linearize_iterative(lst):
    result = []
    stack = [lst]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(reversed(current))
        else:
            result.append(current)
    return result   

# 2) Функция для расчёта
def sequence_recursive(k):
    if k == 1:
        return (1, 1)
    a_prev, b_prev = sequence_recursive(k - 1)
    return (2 * b_prev + a_prev, 2 * a_prev + b_prev)

def sequence_iterative(k):
    a, b = 1, 1
    for nothing in range(2, k + 1):
        a, b = 2 * b + a, 2 * a + b
    return a, b

# print(linearize_recursive([1, 2, [3, 4, [5, [6, []]]]]))
#print(linearize_iterative([1, 2, [3, 4, [5, [6, []]]]]))
print(sequence_recursive(5))
#print(sequence_iterative(5))