def solution(digits):
    number_str = str(digits)
    numbers_list = []
    last_four = len(number_str) - 4

    for num in range(0, last_four):
        num = int(number_str[num:(num+5)])
        numbers_list.append(num)

    numbers_list.sort()
    return numbers_list[-1]

print(solution('1234567898765'))