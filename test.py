# def word(word1, word2)-> str:
#     new_string = ''
#     for x in word1:
#
#     return new_string
# string1 = 'ade'
# string2 = 'seyi'
# print(word(string1, string2))

def test(s)->str:
    array = s.split(' ')
    new_str = array[::-1]
    return new_str

str = 'esther is going'
print(test(str))
