with open('input1.txt') as num_file:
    num_list = [int(i) for i in num_file.readlines()]

for i in range(len(num_list)):
    num = num_list[i]

    for j in range(1,len(num_list)-i):
        num2 = num_list[i+j]

        for k in range(2,len(num_list)-i-j):
            if num + num2 + num_list[i+j+k] == 2020:
                second_num = num_list[i+j]
                first_num = num
                third_num = num_list[i+j+k]
                break
            else:
                continue

print(first_num * second_num * third_num)
