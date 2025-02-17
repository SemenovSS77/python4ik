# -*- coding: utf-8 -*-

from distance00 import ddistance
from circle01 import ccircle
from operations02 import ooperations


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