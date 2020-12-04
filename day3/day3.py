from operator import mul  # imports the * operator as mul
from functools import reduce

with open('input.txt') as file:
    lines = file.readlines()


def tree_count(slope):
    # print('new call', '-'*8)
    ans = 0
    x = -slope[0]
    y = 0
    for line in lines:
        if y > 1:
            y -= 1
            continue
        line = line.strip()
        x = (x+slope[0]) % len(line)
        if line[x] == '#':
            ans += 1
        # newline = list(line)
        # newline[x] = 'O'
        # newline = ''.join(newline)
        y = slope[1]
        # print(newline.strip())
    return ans


def main():
    list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    a = [tree_count(a) for a in list]
    print(a)
    a = reduce(mul, a) # reduce : reduces or folds an iterable. applies a
                        # function (first param) to the 2nd param, to produce
                        # a partial result, and then does the same using the
                        # partial result and the 3rd item, and so on
    print(a)



main()
