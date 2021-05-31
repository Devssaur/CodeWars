#https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python

def repeat_str(repeat, string):
    nome =""
    for item in range (repeat):
        nome += string
       # print(item)
    return nome

print(repeat_str(6, "I")) # "IIIIII"