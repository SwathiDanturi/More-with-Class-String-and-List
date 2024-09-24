*** File**: Design.md
*** Design for all the sentence methods ***
*** Created**: September 2024
*** Developer**: Swathi Danturi
*** Date**: 9/23/2024

### Design of `my_split()` core function
- define `my_split()` method and `self` the current instance of the class `Sentence` is the only parameter
- `self.sentence`is an instance variable of the class `Sentence` and is initialized to a string in the constructor, which is passed as an argument when the class instance is created
- use the instance variable `self.words` as an accumulator to store the list of words from string split
- declare `a_word` an accumulator to store the words from `self.sentence` and initialize it to an empty string
- `for` each character `char` in `self.sentence`, iterate through the following statements:
    - check if `char` is space `' '`
    - if `char` is not a space then:
        - add `char` to the `a_word`, an accumulator of type string to store the characters
    - else:
        - if `a_word` is not empty then:
            - append `a_word` to `self.words`
            - empty `a_word` by assigning an empty string to it
- if `a_word` is not empty then append it to `self.word`