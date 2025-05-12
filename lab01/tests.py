# -*- coding: utf-8 -*-

from distance00 import ddistance
from circle01 import ccircle
from operations02 import ooperations
from favorite_movies03 import ffavorite_movies
from my_family04 import mmy_family
from zoo05 import zzoo
from songs_list06 import ssongs_list
from secret07 import ssecret
from garden08 import ggarden
from shopping09 import sshopping
from store10 import sstore


def test_ddistance(capsys):
    ddistance()
    captured = capsys.readouterr()
    expected_output = "{'Moscow': {'London': 145.60219778561037, 'Paris': 130.38404810405297}, 'London': {'Moscow': 145.60219778561037, 'Paris': 42.42640687119285}, 'Paris': {'Moscow': 130.38404810405297, 'London': 42.42640687119285}}\n"
    assert captured.out == expected_output

def test_ccircle(capsys):
    ccircle()
    captured = capsys.readouterr()
    expected_output = "5541.7693\nTrue\nFalse\n"
    assert captured.out == expected_output

def test_ooperations(capsys):
    ooperations()
    captured = capsys.readouterr()
    expected_output = "9\n25\n"
    assert captured.out == expected_output

def test_ffavorite_movies(capsys):
    ffavorite_movies()
    captured = capsys.readouterr()
    expected_output = "\n Терминатор \n Назад в будущее \n Пятый элемент \n Чужие\n"
    # "\n", film1, "\n", last_film, "\n", film2, "\n", rfilm2
    assert captured.out == expected_output

def test_mmy_family(capsys):
    mmy_family()
    captured = capsys.readouterr()
    expected_output = "Рост мамы - 170 см\nОбщий рост моей семьи - 530 см\n"
    assert captured.out == expected_output


def test_zzoo(capsys):
    zzoo()
    captured = capsys.readouterr()
    expected_output = (
        "['lion', 'bear', 'kangaroo', 'elephant', 'monkey']\n"
        "['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']\n"
        "['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']\n"
        "Лев сидит в клетке 1\nЖаворонок сидит в клетке 7\n"
    )
    assert captured.out == expected_output


def test_ssongs_list(capsys):
    ssongs_list()
    captured = capsys.readouterr()
    expected_output = (
        "Три песни звучат 14.93 минут\n"
        "А другие три песни звучат 13.49 минут\n"
    )
    assert captured.out == expected_output


def test_ssecret(capsys):
    ssecret()
    captured = capsys.readouterr()
    expected_output = "в бане веник дороже денег\n"
    assert captured.out == expected_output


def test_ggarden(capsys):
    ggarden()
    captured = capsys.readouterr()
    # Множества неупорядочены, поэтому проверяем через sorted
    output_lines = captured.out.split('\n')
    assert sorted(output_lines[0].strip("{}").replace("'", "").split(', ')) == sorted(['ромашка', 'подсолнух', 'роза', 'одуванчик', 'гладиолус', 'клевер', 'мак'])
    assert sorted(output_lines[1].strip("{}").replace("'", "").split(', ')) == sorted(['ромашка', 'одуванчик'])
    assert sorted(output_lines[2].strip("{}").replace("'", "").split(', ')) == sorted(['подсолнух', 'роза', 'гладиолус'])
    assert sorted(output_lines[3].strip("{}").replace("'", "").split(', ')) == sorted(['клевер', 'мак'])


def test_sshopping(capsys, monkeypatch):
    inputs = ["шоколад", "ашан", "89.99", "магнит", "79.99"]
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    sshopping()
    captured = capsys.readouterr()
    assert "'шоколад': [{'shop': 'ашан', 'price': 89.99}, {'shop': 'магнит', 'price': 79.99}]" in captured.out


def test_sstore(capsys):
    sstore()
    captured = capsys.readouterr()
    expected_output = (
        "Лампа - 27 шт, стоимость 1134 руб\n"
        "Стол - 54 шт, стоимость 27860 руб\n"
        "Диван - 3 шт, стоимость 3550 руб\n"
        "Стул - 105 шт, стоимость 10311 руб\n"
    )
    assert captured.out == expected_output