def lovefunc(flower1, flower2 ):
    f_1 = flower1 % 2
    f_2 = flower2 % 2
    if f_1 == 1 and f_2 == 0:
        return True
    elif f_1 == 0 and f_2 == 1:
        return True
    else:
        return False