#!-*- conding: utf8 -*-
import random

from pip._vendor.distlib.compat import raw_input

while True:
    for x in range(1):
        print(random.randint(1, 6))

    resp = raw_input("Voce quer jogar novamente? s/n ")

    if resp == 'n':
        break
