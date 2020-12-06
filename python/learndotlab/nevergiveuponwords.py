#!/usr/bin/env python3

import sys

def get_valid_words():
    valid_words = []

    with open('/usr/share/dict/american-english', 'r') as f:
        for line in f:
            word = line.strip()
            valid_words.append(word)

    return valid_words


def remove_invalid_words(filename):
    output = []
    valid_words = get_valid_words()

    with open(filename, 'r') as f:
        # Iterate over each line in the file
        for line in f:
            valid_lyrics = []

            # Look at each word in the line
            for word in line.split():
                if word.lower() in valid_words:
                    valid_lyrics.append(word)

            # Create a string with the valid words separated by spaces
            # https://docs.python.org/3/library/stdtypes.html#str.join
            valid_line = ' '.join(valid_lyrics)

            # Add the valid line to the output
            output.append(valid_line)

    # Join all the valid lines, using a newline character as the seperator
    return '\n'.join(output)


def main():
    # Get the filename passed to the script
    filename = sys.argv[1]

    english_words = get_valid_words()
    lyrics = remove_invalid_words(filename)

    print(lyrics)


if __name__ == '__main__':
    main()
