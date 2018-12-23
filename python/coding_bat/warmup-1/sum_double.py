def sum_double(a, b):
    '''
    Given two int values, return their sum. 
    Unless the two values are the same, 
    then return double their sum.
    '''
    return (a+b)*2 if a == b else (a + b)

print(sum_double(1, 2)) # 3
print(sum_double(3, 2)) # 5
print(sum_double(2, 2)) # 8