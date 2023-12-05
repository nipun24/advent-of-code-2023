if __name__ == '__main__':
    res = 0

    with open('input.txt', 'r') as f:
        for game in f.readlines():
            game = game.strip()
            max_count = {'red': 0, 'green': 0, 'blue': 0}
            outcomes = game.split(':')[1].split(';')
            r = [i.split(',') for i in outcomes]
            for i in r:
                for j in i:
                    count, color = j.strip().split(" ")
                    max_count[color] = int(count) if max_count[color] < int(count) else max_count[color]

            res += (max_count['red'] * max_count['green'] * max_count['blue'])

        print(res)
