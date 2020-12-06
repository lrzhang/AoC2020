# set operations today
import string

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    lines = ' '.join(lines).split('  ') # groups are separated by blank lines and individuals within a group are just newlines. So this code will join all invidiuals of a group into one element of a list with individuals separated by a space

ans = 0
for line in lines:
    # yes_ans = set() -- for use in part 1
    yes_ans = set(string.ascii_lowercase) # creating empty set. note that saying a = {} is a dict and not a set
    indvs = line.split()
    for word in indvs:
        yes_ans = yes_ans.intersection(set(word)) # .union and .intersection return a new set
        # yes_ans = yes_ans.union(set(word)) -- for use in part 1

    ans += len(yes_ans)

print(ans)
