def pos_neg(a, b, negative):
    '''
    Given 2 int values, return True if one 
    is negative and one is positive. Except 
    if the parameter "negative" is True, then 
    return True only if both are negative.
    '''
    return ((a and b) or negative) if not negative else True

print(pos_neg(1, -1, False)) # True
print(pos_neg(-1, 1, False)) # True
print(pos_neg(-4, -5, True)) # True