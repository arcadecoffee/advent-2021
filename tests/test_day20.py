"""
Tests for Day 20
"""

from day20.module import part_1, part_2, load_image, \
    FULL_INPUT_FILE, TEST_INPUT_FILE

TEST_RESULT_0 = """
#..#.
#....
##..#
..#..
..###
"""
TEST_RESULT_0 = TEST_RESULT_0[1:-1]

TEST_RESULT_0_1 = """
.......
.#..#..
.#.....
.##..#.
...#...
...###.
.......
"""
TEST_RESULT_0_1 = TEST_RESULT_0_1[1:-1]

TEST_RESULT_0_5 = """
...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............
"""
TEST_RESULT_0_5 = TEST_RESULT_0_5[1:-1]

TEST_RESULT_1 = """
.##.##.
#..#.#.
##.#..#
####..#
.#..##.
..##..#
...#.#.
"""
TEST_RESULT_1 = TEST_RESULT_1[1:-1]

TEST_RESULT_2 = """
.......#.
.#..#.#..
#.#...###
#...##.#.
#.....#.#
.#.#####.
..#.#####
...##.##.
....###..
"""
TEST_RESULT_2 = TEST_RESULT_2[1:-1]


def test_load():
    img = load_image(TEST_INPUT_FILE)
    assert img.rendered_image == TEST_RESULT_0


def test_margin():
    img = load_image(TEST_INPUT_FILE)
    img.add_margin(1)
    assert img.rendered_image == TEST_RESULT_0_1


def test_margin_5():
    img = load_image(TEST_INPUT_FILE)
    img.add_margin(5)
    assert img.rendered_image == TEST_RESULT_0_5


def test_crop():
    img = load_image(TEST_INPUT_FILE)
    img.add_margin(5)
    img.crop()
    assert img.rendered_image == TEST_RESULT_0


def test_enhance_1():
    img = load_image(TEST_INPUT_FILE)
    img.enhance()
    assert img.rendered_image == TEST_RESULT_1


def test_enhance_2():
    img = load_image(TEST_INPUT_FILE)
    img.enhance(2)
    assert img.rendered_image == TEST_RESULT_2


def test_part_1():
    result = part_1(TEST_INPUT_FILE)
    assert result == 35


def test_part_1_full():
    result = part_1(FULL_INPUT_FILE)
    assert result == 5065


def test_part_2():
    result = part_2(TEST_INPUT_FILE)
    assert result == 3351


def test_part_2_full():
    result = part_2(FULL_INPUT_FILE)
    assert result == 14790
