"""
Tests for Day 16
"""

from day16.module import part_1, part_2, calculate_version_sums, find_value, \
    FULL_INPUT_FILE

TESTS_1 = [
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
    {
        'string': '8A004A801A8002F478',
        'version_sum': 16
    },
    {
        'string': '620080001611562C8802118E34',
        'version_sum': 12
    },
    {
        'string': 'C0015000016115A2E0802F182340',
        'version_sum': 23
    },
    {
        'string': 'A0016C880162017C3686B18A3D4780',
        'version_sum': 31
    },
]

TESTS_2 = [
    {
        'string': 'C200B40A82',
        'value': 3
    },
    {
        'string': '04005AC33890',
        'value': 54
    },
    {
        'string': '880086C3E88112',
        'value': 7
    },
    {
        'string': 'CE00C43D881120',
        'value': 9
    },
    {
        'string': 'D8005AC2A8F0',
        'value': 1
    },
    {
        'string': 'F600BC2D8F',
        'value': 0
    },
    {
        'string': '9C005AC2F8F0',
        'value': 0
    },
    {
        'string': '9C0141080250320F1802104A08',
        'value': 1
    },
]

def test_part_1_0():
    test = TESTS_1[0]
    assert test['version_sum'] == calculate_version_sums(test['string'])


def test_part_1_1():
    test = TESTS_1[1]
    assert test['version_sum'] == calculate_version_sums(test['string'])


def test_part_1_2():
    test = TESTS_1[2]
    assert test['version_sum'] == calculate_version_sums(test['string'])


def test_part_1_all():
    for test in TESTS_1:
        assert test['version_sum'] == calculate_version_sums(test['string'])


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 934


def test_part_2_all():
    for test in TESTS_2:
        assert test['value'] == find_value(test['string'])

def test_part_2_full():
    result = part_2(FULL_INPUT_FILE)
    assert result == 912901337844
