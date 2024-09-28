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
    print('Checking my_split() from client...')
    print('Input is ', s_obj.sentence)
    print('Output is:', s_obj.words)

    s_obj = Sentence('just checking')
    new_sentence = s_obj.my_join()
    print('Checking my_join() from client...')
    print('Input is:', s_obj.sentence)
    print('Word list to be joined:', s_obj.words)
    print('Output is:', new_sentence)

    s_obj = Sentence('just checking')
    word_index = s_obj.my_index('checking')
    print('Checking my_index() from client...')
    print('Input is:', s_obj.sentence)
    print('Word List:', s_obj.words)
    print('Word found at index:', word_index)

    s_obj = Sentence('just checking')
    word_popped = s_obj.my_pop(0)
    print('Checking my_pop() from client...')
    print('Input is:', s_obj.sentence)
    print('Word List:', s_obj.words)
    print('Word popped is:', word_popped)


main()
