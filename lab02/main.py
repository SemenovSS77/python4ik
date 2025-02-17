def n1():
    alphabet = ["К", "А", "Т", "Е", "Р"]
    length = 6
    count = len(alphabet) ** (length - 2)
    print(count)

def n2():
    a = 216 ** 6 + 216 ** 4 + 36 ** 5 - 6 ** 14 - 24
    count = []
    while a > 0:
        count.append(a % 6)
        a //= 6
    count.reverse()
    print(len(set(count)))

def n3():
    for i in range(123450708,123460000):
        if (i % 23 == 0) and (i % 10 == 8) and ((i // 100) % 10 == 7):
            print(i, i // 23)

choice = input("")
if choice == "n1":
    n1()
if choice == "n2":
    n2()
if choice == "n3":
    n3()