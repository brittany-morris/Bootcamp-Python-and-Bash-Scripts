#!/usr/bin/env python3

import sys
from string import ascii_lowercase

# Rotate each word by the provided shift
def rotate_word(word, shift):
    # Return the word if shift is 0
    if shift == 0:
        return word
    else:
        # String to hold decoded word
        decoded_word = ''

        # Iterate over each letter in the word
        for character in word:
            # We will only shift lowercase letters
            if character in ascii_lowercase:
                # Get the index of the letter in the alphabet
                index = ascii_lowercase.find(character)
                # Shift the index
                shifted_index = (index + shift) % len(ascii_lowercase)
                # Add the decoded letter to the word
                decoded_word += ascii_lowercase[shifted_index]
            else:
                decoded_word += character

        return decoded_word


def decode_sentence(text):
    # List to contain the decoded words
    decoded = list()

    # Iterate over the words in the string
    for shift, word in enumerate(text.split()):
        # Negate the shift since we are shifting left
        shift *= -1

        # Decode each word using it's index in
        # the array as the number of shifted characters
        decoded_word = rotate_word(word, shift)

        # Add each decoded word to the list
        decoded.append(decoded_word)

    # Retun the decoded words separated by a space
    return ' '.join(decoded)


# Return a string containing the file's contents
def get_file_contents(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def main():
    # Get the filename from the command line arguments
    file_name = sys.argv[1]

    # Get the file contents
    file_contents = get_file_contents(file_name)

    # Split the file contents into separate lines
    for line in file_contents.split('\n'):
        # Decode and print each line
        decoded_sentence = decode_sentence(line)
        print(decoded_sentence)


if __name__ == '__main__':
    main()
