def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    result = sq ** (1/2)
    if result.is_integer():
        return (result + 1) ** 2
    else:
        return -1

print(find_next_square(121))