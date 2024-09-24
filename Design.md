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
- if `a_word` is not empty then append it to `self.words`

### Design of `my_join()` core function
- define `my_join()` method and `self` the current instance of the class `Sentence` is the only parameter
- `self.sentence`is an instance variable of the class `Sentence` and is initialized to a string in the constructor, which is passed as an argument when the class instance is created
- call the method `my_split()` to split `self.sentence` and the result list will be stored in `self.words` (this is the functionality of `my_split()`)
- declare an accumulator `joined_string` and initialize it to an empty string to store the concatenated string of the word list `self.words`
- for each `word` in `self.words`, iterate through the following:
    - concatenate `word` to `joined_string` using `+` operator
    - check if `word` is the last word in the list using reverse indexing:
        - if it is not the last word, then add a space `' '` to `joined_string`
- return the concatenated string `joined_string` of the word list `self.words`