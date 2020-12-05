# lots of regex today
# * is greedy match for chars
# ^ and $ are anchors for beginning and end
# [0-9] brackets are for ranges for a single char
# (one|two) parentheses are grouping and | is or
# best do       a= re.compile(regex)
#               match = a.match(string) --> returns match object taht you can
#               match.group() to get a printout of the regexs, None if DNE

import re
import pdb

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]

lines = ' '.join(lines).split('  ')

valid = 0
for line in lines:
    ans = 0
    byr = line.find('byr:')
    iyr = line.find('iyr:')
    eyr = line.find('eyr:')
    hgt = line.find('hgt')
    hcl = line.find('hcl:')
    ecl = line.find('ecl:')
    pid = line.find('pid:')
    cid = line.find('cid:')


    val = [byr, iyr, eyr, hgt, hcl, ecl, pid]
    if -1 in val:
        continue

    print(line)

    if 1920 <= int(line[byr+4:byr+8]) <= 2002:
        ans += 1
    if 2010 <= int(line[iyr+4:iyr+8]) <= 2020:
        ans += 1
    if 2020 <= int(line[eyr+4:eyr+8]) <= 2030:
        ans += 1

    cm = line.find('cm', hgt, len(line))
    inch = line.find('in',hgt, len(line))

    #re_hgt = re.compile('[0-9]*(in|cm)')
    # * is greedy match so 0-infinity of numbers followed by in or cm, parentheses groups the chars)

    re_hgt = re.compile('[0-9]{2,3}(in|cm)')
    match_hgt = re_hgt.match(line[hgt+4:hgt+9])
    if match_hgt:
        if cm == -1:
            if 59 <= int(line[hgt+4:inch]) <= 76:
                ans += 1

        if inch == -1:
            if 150 <= int(line[hgt+4:cm]) <= 193:
                ans += 1

    re_hcl = re.compile('#\w{6,6}') # creates a pattern object that matches #, \w alphanumeric exactly 6 times
    match_hcl = re_hcl.match(line[hcl+4:hcl+11]) # creates a match object if there is a match, None otherwise
    if match_hcl:
        ans += 1

    colors = ['amb','blu','brn','gry','grn','hzl','oth']
    if line[ecl+4:ecl+7] in colors:
        ans += 1

    re_pid = re.compile('[0-9]{9,9}$') # \d == [0-9]
    match_pid = re_pid.match(line[pid+4:pid+13])
    if match_pid:
        ans += 1
    if ans == 7:
        valid += 1

print(valid)
