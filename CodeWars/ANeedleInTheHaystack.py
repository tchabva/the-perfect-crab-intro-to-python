def find_needle(haystack):
    count = 0
    for word in haystack:
        if word == "needle":
            return f"found the needle at position {count}"
        count += 1