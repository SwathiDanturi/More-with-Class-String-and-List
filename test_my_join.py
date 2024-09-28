"""
Test my_join method of sentence
File: test_my_join.py
Created: September 2024
Developer: Swathi Danturi
Date: 9/23/2024
"""

import pytest

from sentence import Sentence


def test_my_join_chars_digits():
    """
    Test string that has characters and digits
    """
    sentence_obj = Sentence('Branch is ahead of 4 commits')
    expected = 'Branch is ahead of 4 commits'
    actual = sentence_obj.my_join()
    assert actual == expected


def test_my_join_extra_spaces():
    """
    Test string that has extra spaces
    """
    sentence_obj = Sentence(' my_join method    implementation   ')
    expected = 'my_join method implementation'
    actual = sentence_obj.my_join()
    assert actual == expected


def test_my_join_one_word():
    """
    Test string that has only one word
    """
    sentence_obj = Sentence('A_Word')
    expected = 'A_Word'
    actual = sentence_obj.my_join()
    assert actual == expected


def test_my_join_empty_string():
    """
    Test string that is an empty string
    """
    sentence_obj = Sentence('')
    expected = ''
    actual = sentence_obj.my_join()
    assert actual == expected


pytest.main()
