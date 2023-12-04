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


if __name__ == '__main__':
    print('Part 1:', part1())
