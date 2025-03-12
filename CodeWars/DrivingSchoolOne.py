def passed(lst):
    passed = []
    for score in lst:
        if score < 19:
            passed.append(score)

    if len(passed) > 0:
        avg = sum(passed) / (len(passed))
        return round(avg)
    else:
        return 'No pass scores registered.'

print(passed([10,10,10,18,20,20]))