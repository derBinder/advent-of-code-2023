if __name__ == '__main__':
    file = open('day1/input.in').read()
    rows = file.split('\n')
    result = 0

    for row in rows:
        calibrationValues = ''
        numbers = []

        for char in list(row):
            if char.isnumeric():
                numbers.append(char)

        calibrationValues = numbers[0] + numbers[-1]
        result = result + int(calibrationValues)

    print(result)
