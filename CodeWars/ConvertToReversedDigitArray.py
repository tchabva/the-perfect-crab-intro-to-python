def digitize(n):
    numbers = []

    for i in str(n):
        numbers.append(int(i))
    numbers.reverse()
    return numbers