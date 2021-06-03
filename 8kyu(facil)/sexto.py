#https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

def get_middle(s):
    num =len(s)/2
    if not num.is_integer():
        return s[int(num)]
    else:
        return s[int(num-1)] + s[int(num)]