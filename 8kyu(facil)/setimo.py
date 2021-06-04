#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
def spin_words(sentence):
    final = ""
    total = sentence.split()
    for names in total:
        num = 0
        qnt_name = len(names)
        if qnt_name > 4:
            while num < len(names):
                qnt_name -= 1
                num += 1
                for word in list(names[qnt_name]):
                    final += word
            final += " "
        else:
            final += names + " "
    return final[0:len(sentence)]

print(spin_words("in sekat dessap one gnirts tneserp"))
