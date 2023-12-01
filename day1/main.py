file = open('day1/input.in').read()
rows = file.split('\n')


def part1():
    result = 0

    for row in rows:
        numbers = []

        for char in list(row):
            if char.isnumeric():
                numbers.append(char)

        result += int(numbers[0] + numbers[-1])
    return result


def part2():
    written_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    result = 0

    for row in rows:
        numbers = []
        buffer = ''

        for char in list(row):
            if char.isnumeric():
                numbers.append(char)

            buffer += char

            for key, value in written_numbers.items():
                if buffer.find(key) != -1:
                    numbers.append(value)
                    buffer = buffer[buffer.find(key) + len(key) - 1:]

        result += int(numbers[0] + numbers[-1])
    return result


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
