#!/usr/bin/env python3

import sys
import hashlib
from string import ascii_lowercase, digits, punctuation, whitespace


def get_full_text(sha1hash, partial_text):
    # Possible characters
    character_set = ascii_lowercase + digits + punctuation + whitespace

    # Generate all possible 4 character strings from the character set
    for frst in character_set:
        # Replace the first underscore
        first_char_replaced = partial_text.replace('_', frst, 1)
        for scnd in character_set:
            # Replace the second underscore
            scnd_char_replaced = first_char_replaced.replace('_', scnd, 1)
            for thrd in character_set:
                # Replace the third underscore
                thrd_char_replaced = scnd_char_replaced.replace('_', thrd, 1)
                for frth in character_set:
                    # Replace the final underscore
                    all_chars_replaced = thrd_char_replaced.replace('_', frth, 1)
                    # Generate SHA1 hash for string with all underscores replaced
                    possible_hash = hashlib.sha1(all_chars_replaced.encode()).hexdigest()

                    # Return the string with the replacements if we find the hash
                    if possible_hash == sha1hash:
                        return all_chars_replaced

    return 'No solution found'


def process_file(file_name):
    # Dictionary to store hashes and the partial text
    hashes = dict()

    with open(file_name, 'r') as f:
        # Iterate over each line in the file
        for line in f:
            line = line.strip()
            # Split the line into the text and the hash
            text, sha1hash = line.split('. sha1hash:')
            # Add the strings to the dictionary with the hash as the key
            hashes[sha1hash] = text

    return hashes


def main():
    # Get filename
    file_name = sys.argv[1]
    # Get hashes and partial text from file
    hashes = process_file(file_name)

    # Iterate through hashes and partial text
    for sha1hash, partial_text in hashes.items():
        # Get full text for hash
        full_text = get_full_text(sha1hash, partial_text)
        print(f'"{full_text}"')


if __name__ == '__main__':
    main()
