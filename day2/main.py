file = open('input.in').read()
rows = file.split('\n')


def part1():
    id_sum = 0
    max_colors = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    for game in rows:
        possible = True
        game_id = game.split(':')[0].split(' ')[1]
        game_sets = game.split(':')[1].split(';')

        for game_set in game_sets:
            colors = game_set.split(',')

            for color in colors:
                color = color.strip()
                count = color.split(' ')[0]
                color_name = color.split(' ')[1]

                if int(count) > max_colors.get(color_name):
                    possible = False
                    break

        if possible:
            id_sum += int(game_id)

    return id_sum


def part2():
    total_power = 0

    for game in rows:
        game_sets = game.split(':')[1].split(';')
        max_needed_cubes = {}
        power = 1

        for game_set in game_sets:
            colors = game_set.split(',')

            for color in colors:
                color = color.strip()
                count = int(color.split(' ')[0])
                color_name = color.split(' ')[1]

                if max_needed_cubes.get(color_name) is None or max_needed_cubes.get(color_name) < count:
                    max_needed_cubes[color_name] = count

        for color in max_needed_cubes.items():
            power *= int(color[1])

        total_power += power
    return total_power


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())
