class TaskN1:
    """
    Класс для решения задачи N1.
    Подсчитывает количество 6-буквенных слов, начинающихся с "К" или "Р",
    содержащих только буквы "К", "А", "Т", "Е", "Р".
    
    Пример использования:
    >>> task = TaskN1()
    >>> task.solve()
    625
    """
    def __init__(self, alphabet=None, length=6):
        self.alphabet = alphabet or ["К", "А", "Т", "Е", "Р"]
        self.length = length
    
    def solve(self):
        """
        Решает задачу и возвращает результат.
        
        >>> TaskN1().solve()
        625
        """
        # Первая буква может быть только "К" или "Р" (2 варианта)
        # Остальные 5 букв могут быть любыми из алфавита
        count = 2 * (len(self.alphabet)) ** (self.length - 1)
        return count


class TaskN2:
    """
    Класс для решения задачи N2.
    Подсчитывает количество различных цифр в шестеричной записи числа.
    
    Пример использования:
    >>> task = TaskN2()
    >>> task.solve()
    4
    """
    def __init__(self, number=None):
        self.number = number or (216**6 + 216**4 + 36**5 - 6**14 - 24)
    
    def solve(self):
        """
        Решает задачу и возвращает результат.
        
        >>> TaskN2().solve()
        4
        """
        a = self.number
        digits = set()
        while a > 0:
            digits.add(a % 6)
            a //= 6
        return len(digits)


class TaskN3:
    """
    Класс для решения задачи N3.
    Находит числа в диапазоне, удовлетворяющие определенным условиям.
    
    Пример использования:
    >>> task = TaskN3(123450708, 123460000)
    >>> for result in task.solve():
    ...     print(result[0], result[1])
    123450798 5367426
    123451718 5367466
    123453788 5367556
    123454708 5367596
    123456778 5367686
    123459768 5367816
    """
    def __init__(self, start=123450708, end=123460000):
        self.start = start
        self.end = end
    
    def solve(self):
        """
        Решает задачу и возвращает список кортежей (число, число//23).
        
        >>> TaskN3(123450708, 123460000).solve()
        [(123450798, 5367426), (123451718, 5367466), (123453788, 5367556), (123454708, 5367596), (123456778, 5367686), (123459768, 5367816)]
        """
        results = []
        for i in range(self.start, self.end + 1):
            if (i % 23 == 0) and (i % 10 == 8) and ((i // 100) % 10 == 7):
                results.append((i, i // 23))
        return results


def main():
    import doctest
    doctest.testmod()

    choice = input("Выберите задачу (n1, n2, n3): ")
    if choice == "n1":
        print(TaskN1().solve())
    elif choice == "n2":
        print(TaskN2().solve())
    elif choice == "n3":
        for num, div in TaskN3().solve():
            print(num, div)


if __name__ == "__main__":
    main()