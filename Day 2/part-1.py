if __name__ == '__main__':
    cube_color = {'red': 12, 'green': 13, 'blue': 14}

    res = 0

    with open('input.txt', 'r') as f:
        for game in f.readlines():
            game = game.strip()
            game_id, outcomes = game.split(':')
            flag = True

            for r in outcomes.split(';'):
                r = r.strip()
                for i in r.split(','):
                    if flag:
                        for color, count in cube_color.items():
                            if color in i:
                                temp = i.replace(color, "").strip()
                                if int(temp) > count:
                                    flag = False
                                    break
            if flag:
                _id = game_id.split(" ")[1].strip()
                res += int(_id)

        print(res)
