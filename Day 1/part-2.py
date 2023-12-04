import re

if __name__ == '__main__':
    digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    numbers = [str(x + 1) for x in range(9)]

    res = list()
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            temp = list()
            first_idx = len(line)
            first_digit = 0
            last_idx = -1
            last_digit = 0
            for digit, value in digits.items():
                for i in re.finditer(digit, line):
                    if i.start() < first_idx:
                        first_idx = i.start()
                        first_digit = value
                    if i.start() > last_idx:
                        last_idx = i.start()
                        last_digit = value

            for num in numbers:
                for i in re.finditer(num, line):
                    if i.start() < first_idx:
                        first_idx = i.start()
                        first_digit = num
                    if i.start() > last_idx:
                        last_idx = i.start()
                        last_digit = num

            res.append(int(f'{first_digit}{last_digit}'))

        print(sum(res))
