if __name__ == '__main__':
    res = list()
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            first_digit = None
            last_digit = None
            for char in line.strip():
                if first_digit is None and char.isdigit():
                    first_digit = char
                elif char.isdigit():
                    last_digit = char
            if last_digit is None:
                last_digit = first_digit
            res.append(int(f'{first_digit}{last_digit}'))

        print(sum(res))
