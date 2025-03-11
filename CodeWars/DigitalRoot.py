def digital_root(n):
    total = 0
    num = n
    num_len = len(str(num))

    if num_len < 2:
        return num

    while num_len > 1:
        for i in str(num):
            total += int(i)
        num = total
        total = 0
        num_len = len(str(num))
    return num

# print(digital_root(16))
print(digital_root(132189))
print(digital_root(493193))
