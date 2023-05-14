def check_pwd(pwd):
    is_lower = False
    is_upper = False
    is_digit = False
    symbol = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=']
    is_symbol = False

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

    # check there is at least one digit
    for i in pwd:
        if i.isdigit():
            is_digit= True
            break
    if is_digit == False:
        return False
    
    # check there is at least one symbol
    for i in pwd:
        for j in symbol:
            if i == j:
                is_symbol = True
                break
    if is_symbol == False:
        return False
    
    return True