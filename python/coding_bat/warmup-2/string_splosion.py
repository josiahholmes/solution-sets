def string_splosion(str):
    '''
    Given a non-empty string like "Code" 
    return a string like "CCoCodCode".
    '''
    explosion = ''

    for idx in range(len(str)):
        explosion += str[:idx+1]
        
    return explosion

print(string_splosion('Code')) # 'CCoCodCode'
print(string_splosion('abc')) # 'aababc'
print(string_splosion('ab')) # 'aab'