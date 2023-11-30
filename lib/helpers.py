# lib/helpers.py
from time import sleep
from sys import stdout

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Exit program!")
    exit()

def scan_print(s,t=0.01):
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(t)
    print()