def find_left(arr, x, y, num=''):
    y -= 1
    while y >= 0:
        if arr[x][y].isdigit():
            num += arr[x][y]
            y -= 1
        else:
            return num[::-1]
    return num[::-1]


def find_right(arr, x, y, _shape, num=''):
    y += 1
    while y < _shape[1]:
        if arr[x][y].isdigit():
            num += arr[x][y]
            y += 1
        else:
            return num
    return num


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        schematic = list()
        temp = list()
        for data in f.read():
            if data == '\n':
                schematic.append(temp)
                temp = list()
            else:
                temp.append(data)
        if len(temp):
            schematic.append(temp)

        shape = [len(schematic), len(schematic[0])]
        res = 0
        for i in range(shape[0]):
            for j in range(shape[1]):
                gears = list()
                count = 0
                if schematic[i][j] == '*':
                    # look to the left
                    if j > 0 and schematic[i][j - 1].isdigit():
                        count += 1
                        it = schematic[i][j - 1]
                        left = find_left(schematic, i, j - 1)
                        right = ''
                        full = left + it + right
                        gears.append(int(full))
                    # look to the right
                    if j < shape[1] - 1 and schematic[i][j + 1].isdigit():
                        count += 1
                        it = schematic[i][j + 1]
                        left = ''
                        right = find_right(schematic, i, j + 1, shape)
                        full = left + it + right
                        gears.append(int(full))
                    # look to the up
                    if i > 0:
                        if schematic[i - 1][j].isdigit():
                            count += 1
                            it = schematic[i - 1][j]
                            left = find_left(schematic, i - 1, j)
                            right = find_right(schematic, i - 1, j, shape)
                            full = left + it + right
                            gears.append(int(full))
                        else:
                            # look up left
                            if j - 1 > 0 and schematic[i - 1][j - 1].isdigit():
                                count += 1
                                it = schematic[i - 1][j - 1]
                                left = find_left(schematic, i - 1, j - 1)
                                right = ''
                                full = left + it + right
                                gears.append(int(full))
                            # look up right
                            if j + 1 > 0 and schematic[i - 1][j + 1].isdigit():
                                count += 1
                                it = schematic[i - 1][j + 1]
                                left = ''
                                right = find_right(schematic, i - 1, j + 1, shape)
                                full = left + it + right
                                gears.append(int(full))
                    # look to the down
                    if i < shape[0] - 1:
                        if schematic[i + 1][j].isdigit():
                            count += 1
                            it = schematic[i + 1][j]
                            left = find_left(schematic, i + 1, j)
                            right = find_right(schematic, i + 1, j, shape)
                            full = left + it + right
                            gears.append(int(full))
                        else:
                            # look down left
                            if j - 1 > 0 and schematic[i + 1][j - 1].isdigit():
                                count += 1
                                it = schematic[i + 1][j - 1]
                                left = find_left(schematic, i + 1, j - 1)
                                right = ''
                                full = left + it + right
                                gears.append(int(full))
                            # look down right
                            if j + 1 > 0 and schematic[i + 1][j + 1].isdigit():
                                count += 1
                                it = schematic[i + 1][j + 1]
                                left = ''
                                right = find_right(schematic, i + 1, j + 1, shape)
                                full = left + it + right
                                gears.append(int(full))

                if count == 2:
                    res += (gears[0] * gears[1])

        print(res)
