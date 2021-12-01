def part1() -> int:
    increases = 0

    with open('input.txt') as f:
        prev = int(next(f))
        for curr in f:
            curr = int(curr)
            increases += int(curr > prev)
            prev = curr

    return increases


def part2() -> int:
    increases = 0

    with open('input.txt') as f:
        prev_set = [int(next(f)) for x in range(3)]
        for val in f:
            curr_set = prev_set[1:] + [int(val)]
            increases += int(sum(curr_set) > sum(prev_set))
            prev_set = curr_set

    return increases


if __name__ == '__main__':
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')
