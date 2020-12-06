#!/usr/bin/env python3

import sys


# Read the provided file and return a dictionary with dates serving as keys,
# and the value of each key being the titles that were released on that date
def get_title_release_dates(filename):
    release_dates = {}

    with open(filename, 'r') as f:
        # Read one line of the file to skip the header line in the file
        header_line = f.readline()

        for line in f:
            # Get the title, publisher, and date fields from the line
            # Store the rest of the fields in a variable named 'misc'
            title, publisher, date, *misc = line.split(',')

            if date not in release_dates:
                # Create a list to hold all titles released on that date
                release_dates[date] = []

            # Append the current title to the list
            release_dates[date].append(title)

    return release_dates


def main():
    filename = sys.argv[1]
    release_dates = get_title_release_dates(filename)

    # Sort the dictionary by release date
    for date in sorted(release_dates.keys()):
        # Sort the titles released on that day
        for title in sorted(release_dates[date]):
            # If the title is longer than 15 characters shorten it
            if len(title) > 15:
                title = title[:14] + '~'

            # Print the titles right-aligned, in a column 15 characters wide followed by the date
            # https://docs.python.org/3/library/string.html#format-specification-mini-language
            print(f'{title[:15]:>15} {date}')


if __name__ == '__main__':
    main()
