"""
File: client.py
Initial developers: COMP 801 instructors
Developer: Swathi Danturi
Date:09/23/2024
"""
from sentence import Sentence


def main():
    """
    Check functionality of `Sentence` class.
    """
    s_obj = Sentence('just chekcing')
    print(s_obj.sentence)
    print(s_obj.words)


main()
