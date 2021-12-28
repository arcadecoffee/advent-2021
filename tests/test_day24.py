"""
Tests for Day 24
"""

from day24.module import ArithmeticLogicUnit, load_data, check_version_number, part_1, part_2, \
    FULL_INPUT_FILE, TEST1_INPUT_FILE, TEST2_INPUT_FILE, TEST3_INPUT_FILE


def test_alu_1():
    alu = ArithmeticLogicUnit()
    alu.execute(load_data(TEST1_INPUT_FILE), [42])
    assert alu.x == -42


def test_alu_2():
    alu = ArithmeticLogicUnit()
    alu.execute(load_data(TEST2_INPUT_FILE), [2, 6])
    assert alu.z == 1

    alu.execute(load_data(TEST2_INPUT_FILE), [2, 5])
    assert alu.z == 0


def test_alu_3():
    alu = ArithmeticLogicUnit()
    alu.execute(load_data(TEST3_INPUT_FILE), [42])
    assert alu.w == 1
    assert alu.x == 0
    assert alu.y == 1
    assert alu.z == 0


def test_check_version_number():
    instructions = load_data(FULL_INPUT_FILE)
    assert check_version_number(instructions, 39494195799979)
    assert check_version_number(instructions, 13161151139617)


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 39494195799979


def test_part_2_full():
    result = part_2(FULL_INPUT_FILE)
    assert result == 13161151139617
