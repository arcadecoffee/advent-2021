"""
Tests for Day 8
"""

from day08.module import deduce_dictionary, decode_message, part_1, part_2, \
    FULL_INPUT_FILE, TEST_INPUT_FILE

simple_dictionary = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}


def test_deduce():
    dictionary = deduce_dictionary(' '.join(simple_dictionary.values()))
    set_dictionary = {}
    for i in simple_dictionary:
        set_dictionary[i] = set(simple_dictionary[i])
    assert dictionary == set_dictionary


def test_decode_message():
    coded_input = ' '.join(simple_dictionary.values()) + ' | ' + \
        ' '.join([simple_dictionary[4], simple_dictionary[0],
                  simple_dictionary[2], simple_dictionary[8]])

    result = decode_message(coded_input)
    assert result == '4028'


def test_part_1():
    """
    Result should be: 26
    """
    result = part_1(TEST_INPUT_FILE)
    assert result == 26


def test_part_1_full():
    """
    Result should be: 390
    """
    result = part_1(FULL_INPUT_FILE)
    assert result == 390


def test_part_2():
    """
    Result should be: 61229
    """
    result = part_2(TEST_INPUT_FILE)
    assert result == 61229


def test_part_2_full():
    """
    Result should be: 1011785
    """
    result = part_2(FULL_INPUT_FILE)
    assert result == 1011785
