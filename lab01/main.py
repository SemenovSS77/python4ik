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

choice = input("Номер задания: ")
if choice == "0":
    ddistance()
if choice == "1":
    ccircle()
if choice == "2":
    ooperations()
if choice == "3":
    ffavorite_movies()
if choice == "4":
    mmy_family()
if choice == "5":
    zzoo()
if choice == "6":
    ssongs_list()
if choice == "7":
    ssecret()
if choice == "8":
    ggarden()
if choice == "9":
    sshopping()
if choice == "10":
    sstore()