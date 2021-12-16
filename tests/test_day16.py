"""
Tests for Day 16
"""

from day16.module import part_1, part_2, calculate_version_sums, \
    FULL_INPUT_FILE

TESTS = [
    {
        'string': 'D2FE28',
        'version_sum': int('110', 2)
    },
    {
        'string': '38006F45291200',
        'version_sum': 1 + int('110', 2) + int('010', 2)
    },
    {
        'string': 'EE00D40C823060',
        'version_sum': 7 + int('010', 2) + int('100', 2) + int('001', 2)
    },
    # {
    #     'string': '8A004A801A8002F478',
    #     'version_sum': 16
    # },
    # {
    #     'string': '620080001611562C8802118E34',
    #     'version_sum': 12
    # },
    # {
    #     'string': 'C0015000016115A2E0802F182340',
    #     'version_sum': 23
    # },
    # {
    #     'string': 'A0016C880162017C3686B18A3D4780',
    #     'version_sum': 31
    # },
]


def test_part_1_0():
    test = TESTS[0]
    assert test['version_sum'] == calculate_version_sums(test['string'])


def test_part_1_1():
    test = TESTS[1]
    assert test['version_sum'] == calculate_version_sums(test['string'])


def test_part_1_2():
    test = TESTS[2]
    assert test['version_sum'] == calculate_version_sums(test['string'])


def test_part_1_all():
    for test in TESTS:
        assert test['version_sum'] == calculate_version_sums(test['string'])


# def test_part_1_full():
#     result = part_1(FULL_INPUT_FILE)
#     assert result == 0
#
#
# def test_part_2():
#     result = part_2(TEST_INPUT_FILE)
#     assert result == 0
#
#
# def test_part_2_full():
#     result = part_2(FULL_INPUT_FILE)
#     assert result == 0
