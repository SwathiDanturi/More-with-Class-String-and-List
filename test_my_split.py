"""
Test my_spilt method of sentence
File: test_my_split.py
Created: September 2024
Developer: Swathi Danturi
Date: 9/23/2024
"""

import pytest

from sentence import Sentence


def test_my_split_chars_digits():
    """
    Test string that has characters and digits
    """
    test_string = 'COMP 801.M1 ICP Fall 2024!!'
    sentence_obj = Sentence(test_string)
    expected = ['COMP', '801.M1', 'ICP', 'Fall', '2024!!']
    sentence_obj.my_split()
    actual = sentence_obj.words
    assert actual == expected


def test_my_split_extra_spaces():
    """
    Test string that has extra spaces
    """
    test_string = '  Split function   returns a list       '
    sentence_obj = Sentence(test_string)
    expected = ['Split', 'function', 'returns', 'a', 'list']
    sentence_obj.my_split()
    actual = sentence_obj.words
    assert actual == expected


def test_my_split_one_word():
    """
    Test string that has only one word
    """
    test_string = 'Oneword'
    sentence_obj = Sentence(test_string)
    expected = ['Oneword']
    sentence_obj.my_split()
    actual = sentence_obj.words
    assert actual == expected


def test_my_split_empty_string():
    """
    Test string that is an empty string
    """
    test_string = ''
    sentence_obj = Sentence(test_string)
    expected = []
    sentence_obj.my_split()
    actual = sentence_obj.words
    assert actual == expected


pytest.main()