def not_string(str):
    '''
    Given a string, return a new string 
    where "not " has been added to the front. 
    However, if the string already begins with 
    "not", return the string unchanged.
    '''
    if 'not' not in str[:3]:
        return 'not ' + str
    return str

print(not_string('candy')) # 'not candy'
print(not_string('x')) # 'not x'
print(not_string('not bad')) # 'not bad'