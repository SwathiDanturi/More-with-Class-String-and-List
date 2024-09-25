"""
Test my_index method of sentence
File: test_my_index.py
Created: September 2024
Developer: Swathi Danturi
Date: 9/23/2024
"""

import pytest  # noqa: F401

from sentence import Sentence


def test_my_index_word_found():
    """
    Test string that contains the word to be searched for
    """
    sentence_obj = Sentence('University of New Hampshire, Manchester')
    actual = sentence_obj.my_index('New')
    expected = 2
    assert actual == expected


def test_my_index_word_notfound():
    """
    Test string that does not contain the word to be searched for
    """
    sentence_obj = Sentence('Prepare well for the exam')
    actual = sentence_obj.my_index('New')
    expected = None
    assert actual == expected
