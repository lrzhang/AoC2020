from collections import Counter
import pdb

ans = 0
with open('input.txt') as file:
    for line in file.readlines():

        line = line.split()
        line[0] = [int(i) for i in line[0].split('-')] # [ [x,y], letter, string]
        line[1] = line[1][0:1]

        # code block for part 1 using counter to count the instance of the letter in the string
        # c = Counter(line[2])
        # count = c[line[1]]
        # if count >= line[0][0] and count <= line[0][1]:
        #     ans += 1

        if (line[2][line[0][0]-1] == line[1]) ^ (line[2][line[0][1]-1] == line[1]):
            ans += 1

    print(ans)
