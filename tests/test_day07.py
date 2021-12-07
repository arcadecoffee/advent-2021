"""
Tests for Day 7
"""

from day07.module import calculate_linear_convergence, calculate_nonlinear_convergence, \
    FULL_INPUT_FILE, TEST_INPUT_FILE


def test_part_1():
    """
    Result should be: 37
    """
    result = calculate_linear_convergence(TEST_INPUT_FILE)
    assert result == 37


def test_part_1_full():
    """
    Result should be: 349357
    """
    result = calculate_linear_convergence(FULL_INPUT_FILE)
    assert result == 349357


def test_part_2():
    """
    Result should be: 168
    """
    result = calculate_nonlinear_convergence(TEST_INPUT_FILE)
    assert result == 168


def test_part_2_full():
    """
    Result should be: 96708205
    """
    result = calculate_nonlinear_convergence(FULL_INPUT_FILE)
    assert result == 96708205
