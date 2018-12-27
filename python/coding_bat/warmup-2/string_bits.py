def string_bits(str):
    '''
    Given a string, return a new string made 
    of every other char starting with the first, 
    so "Hello" yields "Hlo".
    '''
    bits = [str[idx] for idx in range(0,len(str),2)]
    return ''.join(bits)


print(string_bits('Hello')) # 'Hlo'
print(string_bits('Hi')) # 'H'
print(string_bits('Heeololeo')) # 'Hello'
