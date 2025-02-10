# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

tables_code = goods["Стол"]
tables1_items = store[tables_code][0]
tables2_items = store[tables_code][1]
tables1_quantity = tables1_items["quantity"]
tables2_quantity = tables2_items["quantity"]
tables_quantity = tables1_items["quantity"] + tables2_items["quantity"]
tables1_price = tables1_items["price"]
tables2_price = tables2_items["price"]
tables_cost = tables1_quantity * tables1_price + tables2_quantity * tables2_price

couches_code = goods["Диван"]
couches1_items = store[couches_code][0]
couches2_items = store[couches_code][1]
couches1_quantity = couches1_items["quantity"]
couches2_quantity = couches2_items["quantity"]
couches_quantity = couches1_items["quantity"] + couches2_items["quantity"]
couches1_price = couches1_items["price"]
couches2_price = couches2_items["price"]
couches_cost = couches1_quantity * couches1_price + couches2_quantity * couches2_price

chairs_code = goods["Стул"]
chairs1_items = store[chairs_code][0]
chairs2_items = store[chairs_code][1]
chairs3_items = store[chairs_code][2]
chairs1_quantity = chairs1_items["quantity"]
chairs2_quantity = chairs2_items["quantity"]
chairs3_quantity = chairs3_items["quantity"]
chairs_quantity = chairs1_items["quantity"] + chairs2_items["quantity"] + chairs3_items["quantity"]
chairs1_price = chairs1_items["price"]
chairs2_price = chairs2_items["price"]
chairs3_price = chairs3_items["price"]
chairs_cost = chairs1_quantity * chairs1_price + chairs2_quantity * chairs2_price + chairs3_quantity * chairs3_price

print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')
print('Диван -', couches_quantity, 'шт, стоимость', couches_cost, 'руб')
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')