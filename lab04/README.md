# Задание 1
## Проделанная работа:
Замыкаем функцию calculate_average для вычисления среднего значения, которая принимает *args.  
Она нам возвращает суммирование, деленное на кол-во элементов, иначе возвращает 0.  
```
def calculate_average(*args):
    return sum(args) / len(args) if args else 0
```

# Задание 2
## Проделанная работа:
Создали функцию check_args с аргументом f, которая оборачивает вложенную функцию wrapper и возвращает её же.  
Функция wrapper вызывается вместо f, принимает произвольное кол-во аргументов (*args) и передает в функцию f,  
если выполняются условия, что наш аргумент является целым числом или числом с плавающей точкой.  
что аргумент находится в диапозоне, который мы указываем. Иначе выдает ошибку.  
```
def check_args(f):
    def wrapper(*args):
        if any(not isinstance(arg, (int, float)) or not (0 <= arg <= 100) for arg in args):
            raise ValueError("Ошибка")
        return f(*args)
    return wrapper
```

# Применение декоратора к замыканию, вывод
## Проделанная работа:
Декорируем функцию вспомощью @check_args.  
Используем try, т.к. понимаем, что код может выдать ошибку. Через except выводим то, что вышла ошибка.  
![image](https://github.com/user-attachments/assets/281cd077-15b0-4eba-a805-c6d659235638)

# Используемые материалы
[Декораторы](https://habr.com/ru/companies/otus/articles/727590/)  
[Замыкания](https://habr.com/ru/articles/862692/)  
[try/except](https://docs.python.org/3/tutorial/errors.html)
