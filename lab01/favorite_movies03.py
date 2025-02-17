# -*- coding: utf-8 -*-

def ffavorite_movies():
    # Есть строка с перечислением фильмов

    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

    # Выведите на консоль с помощью индексации строки, последовательно:
    #   первый фильм
    #   последний
    #   второй
    #   второй с конца

    # Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
    # Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
    # как указано в задании!

    # TODO здесь ваш код

    film1 = my_favorite_movies[0:10]
    last_film = my_favorite_movies[-15:]
    film2 = my_favorite_movies[12:25]
    rfilm2 = my_favorite_movies[-22:-17]
    print("\n", film1, "\n", last_film, "\n", film2, "\n", rfilm2)