# Write a python program that removes all punctuation from a given string.
import string


def remove_punctuation(input_string):
    punctuations = string.punctuation
    no_punct_string = ""
    for char in input_string:

        if char not in punctuations:
            no_punct_string += char
