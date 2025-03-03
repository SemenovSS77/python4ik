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

