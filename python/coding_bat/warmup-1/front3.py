def front3(str):
    '''
    Given a string, we'll say that the 
    front is the first 3 chars of the string. 
    If the string length is less than 3, the 
    front is whatever is there. Return a new 
    string which is 3 copies of the front.
    '''
    front = len(str) if (len(str) < 3) else 3
    return str[:front] * 3


print(front3('Java')) # 'JavJavJav'
print(front3('Chocolate')) # 'ChoChoCho'
print(front3('abc')) # 'abcabcabc'
