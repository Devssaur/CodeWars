#https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    """ Transform the object in form of a phone number"""
    number:str = ""
    c = 0
    for index in n:
        if c == 0:
            number += "("
        if c == 3:
            number += ") "
        if c == 6:
            number += "-"
        number += str(index)
        c += 1
    return number

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))