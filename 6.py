def middle_char(text):
    length = len(text)
    mid = length // 2

    if length % 2 == 0:
        return text[mid - 1: mid + 1]
    else:
        return text[mid]
print(middle_char("hello"))     
print(middle_char("test"))      
