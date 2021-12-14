"""
Tests for Day 14
"""

from collections import Counter

from day14.module import part_1, part_2, template_expander, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_template_expander():
    assert ''.join(template_expander(TEST_INPUT_FILE, 0)) == 'NNCB'
    assert ''.join(template_expander(TEST_INPUT_FILE, 1)) == 'NCNBCHB'
    assert ''.join(template_expander(TEST_INPUT_FILE, 2)) == 'NBCCNBBBCBHCB'
    assert ''.join(template_expander(TEST_INPUT_FILE, 3)) == 'NBBBCNCCNBBNBNBBCHBHHBCHB'
    assert ''.join(template_expander(TEST_INPUT_FILE, 4)) == \
           'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
    assert len(''.join(template_expander(TEST_INPUT_FILE, 5))) == 97
    assert len(''.join(template_expander(TEST_INPUT_FILE, 10))) == 3073


def test_template_expander_counts():
    c = Counter(template_expander(TEST_INPUT_FILE, 10))
    assert c['B'] == 1749
    assert c['C'] == 298
    assert c['H'] == 161
    assert c['N'] == 865


def test_part_1():
    """
    Result should be: 1588
    """
    result = part_1(TEST_INPUT_FILE)
    assert result == 1588


def test_part_1_full():
    """
    Result should be: 2891
    """
    result = part_1(FULL_INPUT_FILE)
    assert result == 2891


def test_part_2():
    """
    Result should be: 0
    """
    result = part_2(TEST_INPUT_FILE)
    assert result == 0


def test_part_2_full():
    """
    Result should be: 0
    """
    result = part_2(FULL_INPUT_FILE)
    assert result == 0
