from os import system
from time import sleep


def print_quitting_animation():
    """ Prints animation when quitting the program"""
    system('clear')
    print(f"""\
    QUITTING...
    """)
    sleep(1)
    print(f"""\
    Thanks for using this program!
    """)
    sleep(1)
    print(f"""\
    Made by: 
    """)
    sleep(1)
    print(f"""\
    - Iuliia Konovalova
    """)
    sleep(1)
    print(f"""\
  * for educational purposes only
    """)