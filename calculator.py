#!/usr/bin/env python

import sys

def Calculator():
    number = input("Enter a number or a letter to exit ")
    try:
        xliczba = int(number)

        operator = input("Enter an operation ")

        secondnumber = input("Enter another number ")
        yliczba = int(secondnumber)

        obliczenia(number, secondnumber, operator)
    except ValueError:
        exit()

def obliczenia(xliczba, yliczba, operator):
    xliczba = int(xliczba)
    yliczba = int(yliczba)

    if operator == "+":
        wynik = xliczba + yliczba
        print("Result: ", wynik)
        print (" ")

    elif operator == "-":
        wynik = xliczba - yliczba
        print("Result: ", wynik)
        print (" ")

    elif operator == "*":
        wynik = xliczba * yliczba
        print("Result: ", wynik)
        print (" ")

    elif operator == "/":
        wynik = xliczba / yliczba
        print("Result: ", wynik)
        print (" ")

    elif operator == "**":
        wynik = xliczba ** yliczba
        print("Result: ", wynik)
        print (" ")


i = 1
while i == 1:
    Calculator()
