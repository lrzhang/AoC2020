import pdb

with open('input.txt') as file:
    lines = [line.strip() for line in file.readlines()]


id = []

# lines = ['BFFFFFFLLL']
for line in lines:
    row_val = 0
    col_val = 0


    row = line[0:7]
    column = line[7:10]

    # handling rows. B = back half. F = front half. similar to buddy system (binary space partitioning)
    row = enumerate(row)  # list out the enum obj creates a list of tuples with index# and the value. reverse the row because the first value should be the 2^6


    for power, letter in list(row):
        # print(power, letter)
        if letter == 'B':
            row_val += 2**(6-power)

    column = enumerate(column)
    for power, letter in list(column):
        if letter == 'R':
            col_val += 2**(2-power)

    #print(row_val, col_val)
    curr_id = row_val*8 + col_val
    id.append(curr_id)


def missing_seat(arr):
    val = arr[0]
    i = 0
    missing = []
    while i < len(arr):
        # pdb.set_trace()
        if val == arr[i]:
            pass
        else:
            missing.append(val)
        val += 1
        i += 1
    return missing

id = sorted(id)
print(id)
a = missing_seat(id)
b = missing_seat(a)
print(a)
print(b)
