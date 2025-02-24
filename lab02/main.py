def n1():
    """
    >>> n1()
    625
    """
    alphabet = ["К", "А", "Т", "Е", "Р"]
    length = 6
    count = len(alphabet) ** (length - 2)
    print(count)

def n2():
    """
    >>> n2()
    4
    """
    a = 216 ** 6 + 216 ** 4 + 36 ** 5 - 6 ** 14 - 24
    count = []
    while a > 0:
        count.append(a % 6)
        a //= 6
    count.reverse()
    print(len(set(count)))

def n3():
    """
    >>> n3()
    123450798 5367426
    123451718 5367466
    123453788 5367556
    123454708 5367596
    123456778 5367686
    123459768 5367816
    """
    for i in range(123450708, 123460000):
        if (i % 23 == 0) and (i % 10 == 8) and ((i // 100) % 10 == 7):
            print(i, i // 23)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    choice = input("")
    if choice == "n1":
        n1()
    if choice == "n2":
        n2()
    if choice == "n3":
        n3()