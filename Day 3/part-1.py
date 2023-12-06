def neighbors(arr, x, y, _shape):
    for x2 in range(x - 1, x + 2):
        for y2 in range(y - 1, y + 2):
            if (-1 < x < _shape[0] and -1 < y < _shape[1] and (x != x2 or y != y2) and
                    (0 <= x2 < _shape[0]) and (0 <= y2 < _shape[1])):
                if not arr[x2][y2].isdigit() and arr[x2][y2] != ".":
                    return True
    return False


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
            num = ""
            symbol = False
            for j in range(shape[1]):
                if schematic[i][j].isdigit():
                    num += schematic[i][j]
                    _symbol = neighbors(schematic, i, j, shape)
                    if symbol is True:
                        symbol = True
                    else:
                        symbol = _symbol
                else:
                    if symbol:
                        res += int(num) if num else 0
                    num = ""
                    symbol = False
            if symbol:
                print(num)
                res += int(num) if num else 0
        print(res)
