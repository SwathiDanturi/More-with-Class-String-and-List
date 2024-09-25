"""
Test my_pop method of sentence
File: test_my_pop.py
Created: September 2024
Developer: Swathi Danturi
Date: 9/23/2024
"""

import pytest

from sentence import Sentence


def test_my_pop_legal_index():
    """
    Test string with a valid index
    """
    sentence_obj = Sentence('Due Date for Assignment is September 25')
    actual = sentence_obj.my_pop(3)
    expected = 'Assignment'
    assert actual == expected


def test_my_pop_not_legal_index():
    """
    Test string with a not valid index
    """
    sentence_obj = Sentence('Make well use of the career fair')
    actual = sentence_obj.my_pop(13)
    expected = None
    assert actual == expected


def test_my_pop_legal_negative_index():
    """
    Test string with a valid negative index
    """
    sentence_obj = Sentence('Due Date for Assignment is September 25')
    actual = sentence_obj.my_pop(-4)
    expected = 'Assignment'
    assert actual == expected


def test_my_pop_not_legal_negative_index():
    """
    Test string with an invalid negative index
    """
    sentence_obj = Sentence('Make well use of the career fair')
    actual = sentence_obj.my_pop(-9)
    expected = None
    assert actual == expected


pytest.main()