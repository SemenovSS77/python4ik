class TaskN1:
    """
    Подсчитывает количество 6-буквенных слов, начинающихся с "К" или "Р",
    содержащих только буквы "К", "А", "Т", "Е", "Р".
    >>> TaskN1().solve()
    625
    """
    def __init__(self, alphabet=None, length=6):
        # Инициализирует алфавит
        self.alphabet = alphabet or ["К", "А", "Т", "Е", "Р"]
        self.length = length
    
    def solve(self):
        # Вычисляет количество возможных 6-буквенных слов по заданным правилам
        count = len(self.alphabet) ** (self.length - 2)
        return count


class TaskN2:
    """
    Подсчитывает количество различных цифр в шестеричной записи числа.
    >>> TaskN2().solve()
    4
    """
    def __init__(self, number=None):
        # Инициализирует число
        self.number = number or (216**6 + 216**4 + 36**5 - 6**14 - 24)
    
    def solve(self):
        # Подсчитывает количество уникальных цифр в шестеричном представлении числа
        a = self.number 
        digits = set()
        while a > 0:
            digits.add(a % 6)
            a //= 6
        return len(digits)


class TaskN3:
    """
    Находит числа в диапазоне, удовлетворяющие определенным условиям.
    >>> TaskN3(123450708, 123460000).solve()
    [(123450798, 5367426), (123451718, 5367466), (123453788, 5367556), (123454708, 5367596), (123456778, 5367686), (123459768, 5367816)]
    """
    def __init__(self, start=123450708, end=123460000):
        # Инициализирует диапазон чисел для поиска
        self.start = start
        self.end = end
    
    def solve(self):
        # Ищет числа в диапазоне, удовлетворяющие условиям:
        # 1. Делится на 23 без остатка
        # 2. Оканчивается на 8
        # 3. Имеет цифру 7 в третьей позиции с конца
        # Возвращает список пар (число, число//23)
        results = []
        for i in range(self.start, self.end + 1):
            if (i % 23 == 0) and (i % 10 == 8) and ((i // 100) % 10 == 7):
                results.append((i, i // 23))
        return results


def main():
    # Запрашиваем у пользователя выбор задачи
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