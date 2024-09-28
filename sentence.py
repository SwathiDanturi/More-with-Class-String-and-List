"""
More practice with class, str, and list concepts.
Initial developers: COMP 801 instructors
File: sentence.py
Updated: Sep 18, 2024
Developer: Swathi Danturi
Date:09/23/2024
"""


class Sentence:
    """
    Encapsulate sentence transformations.
    Instance variables:
    - `self.sentence` of type str
    - `self.words` of type list of strings
    """
    def __init__(self, sentence):
        """
        Create and initialize Sentence object with `sentence`value
        :param sentence: string, has words separated by spaces
        """
        self.sentence = sentence
        self.words = []

    def my_split(self):
        """
        Create a new list with the strings that are the words in
        `self.sentence`. Update `self.words` with this list. This is your
        implementation of Python's`split()' method of the `str` data type.

        Implementation requirement:
        - Do NOT use `split() method.
        """
        a_word = ''
        for char in self.sentence:
            if char != ' ':
                a_word = a_word + char
            else:
                if a_word != '':
                    self.words.append(a_word)
                    a_word = ''
        if a_word != '':
            self.words.append(a_word)

    def my_join(self):
        """
        Create and return a string using the words in `self.words` and
        separating them by a single space. This is your version of Python's
        `join()` method of `str` data type.

        Implementation requriements:
        - Call `self.my_split()` first to assign its return value to
        `self.words`.
        - Do NOT use `join()` method.

        :return: string
        """
        self.my_split()
        new_sentence = ''
        for word in self.words:
            new_sentence += word
            if word != self.words[-1]:
                new_sentence = new_sentence+' '
        return new_sentence

    def my_index(self, a_word):
        """
        Return the index of `a_word` in `self.words`. This is your
        implementation of `index()` method of `list`.
        :param a_word: string
        :return: integer, if `a_word` is found
        :return: None, if not found

        Implementation requirements:
        - Call `self.my_split()` first to assign its return value to
        `self.words`.
        - Do NOT use `index()` method.
        """
        self.my_split()
        index = 0
        for word in self.words:
            if word == a_word:
                return index
            index += 1
        return None

    def my_pop(self, index):
        """
        Return the word from `words` at `index` AND update `self.words` with
        a new list that does not have the word.
        :param index: integer
        :return: string, if `index` is a legal index
        :return: None, if `index` is not a legal index

        Implementation requirements:
        - Call `self.my_split()` first to assign its return value to
        `self.words`.
        - Do NOT use `pop()` method.
        """
        self.my_split()
        words_length = len(self.words)
        if index >= 0 and index >= words_length:
            return None
        elif words_length - index > 2 * words_length:
            return None

        if index < 0:
            index += words_length
        word_at_index = self.words[index]
        self.words = self.words[:index] + self.words[index + 1:]
        return word_at_index
