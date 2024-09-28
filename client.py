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
    s_obj = Sentence('just checking')
    s_obj.my_split()
    print(s_obj.sentence)
    print(s_obj.words)

    s_obj = Sentence('just checking')
    new_sentence = s_obj.my_join()
    print(s_obj.sentence)
    print(s_obj.words)
    print(new_sentence)

    s_obj = Sentence('just checking')
    word_index = s_obj.my_index('checking')
    print(s_obj.sentence)
    print(s_obj.words)
    print(word_index)

    s_obj = Sentence('just checking')
    word_popped = s_obj.my_pop(0)
    print(s_obj.sentence)
    print(s_obj.words)
    print(word_popped)


main()
