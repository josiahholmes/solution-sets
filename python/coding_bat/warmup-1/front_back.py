def front_back(str):
    '''
    Given a string, return a new string 
    where the first and last chars have been exchanged.
    '''
    if len(str) == 1:
        return str
        
    first_char = str[0]
    last_char = str[len(str)-1]
    return last_char + str[1:len(str)-1] + first_char
    

print(front_back('code')) # 'eodc'
print(front_back('a')) # 'a'
print(front_back('ab')) # 'ba'
