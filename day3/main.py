import re

file = open('input.in').read()
rows = file.split('\n')


def get_numbers_from_row(row):
    return [range(idx.start(), idx.end() - 1) for idx in re.finditer(r"\d+", row)]


def get_symbols_from_row(row):
    return [range(idx.start(), idx.end() - 1) for idx in re.finditer(r"[=#+@%*&$/-]", row)]


def is_part(row, number):
    for symbol in get_symbols_from_row(row):
        if symbol.start >= number.start - 1 and symbol.stop <= number.stop + 1:
            return True
    return False


if __name__ == '__main__':
    sum_of_parts = 0

    for row_index, r in enumerate(rows):
        numbers_in_row = get_numbers_from_row(r)

        for number_in_row in numbers_in_row:
            is_part_number = False

            if row_index > 0:
                is_part_number = is_part(rows[row_index - 1], number_in_row)

            if not is_part_number:
                is_part_number = is_part(r, number_in_row)

            if not is_part_number and row_index < len(rows) - 1:
                is_part_number = is_part(rows[row_index + 1], number_in_row)

            if is_part_number:
                sum_of_parts += int(r[number_in_row.start:number_in_row.stop + 1])

    print(sum_of_parts)

