import re


def first_task():
    """
    simplest type of regular expression,  the common letters on each line
    """
    rows = ['abcdefg', 'abcde', 'abc']
    for row in rows:
        if re.search("abc", row):
            print('We found a match! ', row)


def first_and_half_task():
    """
     regular expression, find digits anywhere within the string
    """
    rows = ['abc123xyz', 'define "123', 'var g = 123;']
    for row in rows:
        if re.search("123", row):
            print('We found a match! ', row)


def second_task():
    """
    match first 3 strings, but not fourth.
    """
    rows = ['cat.', '869.', '?=+.', 'abc1']
    for row in rows:
        if re.search("...\.", row):
            print('We found a match! ', row)


def third_task():
    """
    Matching specific characters. Below are a couple lines, where we only want
    to match the first three strings, but not the last three strings.
    """
    rows = ['can', 'man', 'fan', 'dan', 'ran', 'pan']
    for row in rows:
        if re.search("[cfm]an", row):
            print('We found a match! ', row)


def fourth_task():
    """
    Excluding specific characters. With the strings below, try writing a pattern
    that matches only the live animals (hog, dog, but not bog).
    """
    rows = ['hog', 'dog', 'bog']
    for row in rows:
        if re.search("[^b]og", row):
            print('We found a match! ', row)


def fifth_task():
    """
    Character ranges. In the exercise below, notice how all the match and skip lines have a pattern,
    and use the bracket notation to match or skip each character from each line. (Skip last 3)
    """
    rows = ['Ana', 'Bob', 'Cpc', 'aax', 'bby', 'ccz']
    for row in rows:
        if re.search("[A-C][n-p][a-c]", row):
            print('We found a match! ', row)


def sixth_task():
    """
    Catching some zzz's. Try writing a pattern that matches only
    the first two spellings by using the curly brace notation above.
    :return:
    """
    rows = ['wazzzzzup', 'wazzzup', 'wazup']
    for row in rows:
        if re.search("..z{2,5}..", row):
            print('We found a match! ', row)


def seventh_task():
    """
    Mr. Kleene, Mr. Kleene. Below are a few simple strings that you
    can match using both the star and plus metacharacters. Skip last one.
    :return:
    """
    rows = ['aaaabcc', 'aabbbbc', 'aacc', 'a']
    for row in rows:
        if re.search("a+b*c+", row):
            print('We found a match! ', row)


def eighth_tak():
    """
    Characters optional. Try writing a pattern that uses the optionality metacharacter
    to match only the lines where one or more files were found.
    :return:
    """
    rows = ['1 file found?', '2 files found?', '24 files found?', 'No files found.']
    for row in rows:
        if re.search("\d+ files? found\?", row):
            print('We found a match! ', row)


def ninth_task():
    """
    All this whitespace. In the strings below, you'll find that the content of
    each line is indented by some whitespace from the index of the line
    (the number is a part of the text to match). Try writing a pattern
    that can match each line containing whitespace characters between the
    number and the content.
    :return:
    """
    rows = ['1.   abc', '2.	abc', '3.           abc', '4.abc']
    for row in rows:
        if re.search("\d.\s+abc", row):
            print('We found a match! ', row)


def tenth_task():
    """
    Starting and ending. Match first, slip two last.
    :return:
    """
    rows = ['Mission: successful', 'Last Mission: unsuccessful', 'Next Mission: successful upon capture of target']
    for row in rows:
        if re.search("^Mission: successful$", row):
            print('We found a match! ', row)


def eleventh_task():
    """
    Match groups. Go ahead and try to use this to write a regular expression that matches only the
    filenames (not including extension) of the PDF files below.
    :return:
    """
    rows = ['file_record_transcript.pdf', 'file_07241999.pdf', 'testfile_fake.pdf.tmp']
    for row in rows:
        if re.search("^(file_\d*\D*)\.pdf$", row):
            print('We found a match! ', row)


def twelves_task():
    """
    Nested groups. For the following strings, write an expression that
    matches and captures both the full date, as well as the year of the date.
    :return:
    """
    rows = ['Jan 1987', 'May 1969', 'Aug 2011']
    for row in rows:
        if re.search("(\w+ (\d{1,4}))", row):
            print('We found a match! ', row)


def thirteen_task():
    """
    More group work. Below are a couple different common display resolutions,
    try to capture the width and height of each display.
    :return:
    """
    rows = ['1280x720', '1920x1600', '1024x768']
    for row in rows:
        if re.search("(\d+)x(\d+)", row):
            print('We found a match! ', row)


def fourteen_task():
    """
    It's all conditional. Go ahead and try writing a conditional
    pattern that matches only the lines with small fuzzy creatures below.
    :return:
    """
    rows = ['I love cats', 'I love dogs', 'I love logs', '	I love cogs']
    for row in rows:
        if re.search("I love (cats|dogs)", row):
            print('We found a match! ', row)


def fifteen_task():
    """
    Other special characters. Below are a number of different strings, try out the different types of metacharacters or anything we've
    learned in the previous lessons and continue on when you are ready.
    :return:
    """
    rows = ['The quick brown fox jumps over the lazy dog.',
            'There were 614 instances of students getting 90.0% or above.',
            'The FCC had to censor the network for saying &$#*@!.']
    for row in rows:
        if re.search("The.*", row):
            print('We found a match! ', row)


if __name__ == '__main__':
    first_task()
    first_and_half_task()
    second_task()
    third_task()
    fourth_task()
    fifth_task()
    sixth_task()
    seventh_task()
    eighth_tak()
    ninth_task()
    tenth_task()
    eleventh_task()
    twelves_task()
    thirteen_task()
    fourteen_task()
    fifteen_task()