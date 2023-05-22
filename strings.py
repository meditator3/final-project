"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
### git comment
"""
import pytest

def no_duplicates(a_string):

    non_dupe = a_string[0] # first character to compare
    for character in a_string[1:]: # compare to rest of string
        if character not in non_dupe: # add to string only if not already on the non_dupe
            non_dupe += character

    sorted_non_dupe = ''.join(sorted(non_dupe)) # sort method in strings
    return sorted_non_dupe

print(no_duplicates('monty pythons flying circus'))

def reversed_words(a_string):
    reversed_order = []
    string_list = a_string.split(" ") # split the string into a list of words
    for word in string_list[::-1]: # reverse the order and append into a  new list
        reversed_order.append(word)
    return reversed_order

print(reversed_words('monty pythons flying circus'))


def four_char_strings(a_string):
    four_char_words = []
    start_index = 0
    while start_index < len(a_string):
        word = ""
        for index in (start_index, 4+start_index):
            word += a_string[start_index:index]
            if start_index > len(a_string):
                break
        start_index += 4
        four_char_words.append(word)
    return four_char_words
print(four_char_strings('monty pythons flying circus'))
four_char_strings('monty pythons flying circus')

def test_no_duplicates():
    s = 'monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'
test_no_duplicates()

def test_reversed_words():
    s = 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']
test_reversed_words()

def test_four_char_strings():
    s = 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']
test_four_char_strings()

def main():
    return pytest.main(__file__)


if __name__ == '__main__':
    main()
    
