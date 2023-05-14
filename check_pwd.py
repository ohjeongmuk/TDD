def check_pwd(pwd):
    is_lower = False
    is_upper = False

    if len(pwd) < 8 or len(pwd) > 20:
        return False

    # check there is at least one lowerCase
    for i in pwd:
        if i.islower():
            is_lower= True
            break
    if is_lower == False:
        return False

    # check there is at least one UpperCase
    for i in pwd:
        if i.isupper():
            is_upper= True
            break
    if is_upper == False:
        return False

    return True