def makes10(a, b):
    '''
    Given 2 ints, a and b, 
    return True if one of them is 10 
    or if their sum is 10.
    '''
    return ((10 in (a, b)) or (a + b == 10))


print(makes10(9, 10)) # True
print(makes10(9, 9)) # False
print(makes10(1, 9)) # True
