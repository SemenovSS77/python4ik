# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Mother", "Sister", "Me"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["Mother", 170],
    ["Sister", 165],
    ["Me", 195]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print("Рост мамы -", my_family_height[0][1], "см")

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

sum = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1]
print("Общий рост моей семьи -", sum, "см")