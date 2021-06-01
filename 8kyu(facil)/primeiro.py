#https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    paire:int = 0
    turn: int = 0
    for item in list(integers):
        if item > 0 and item % 2 == 1:
            odd = item
            turn += 1
        elif item > 0 and item % 2 == 0:
            paire = item
        elif item< 0 and item % 2 == 0:
            paire = item
        elif item < 0 and item % 2 == 1:
            odd = item
            turn += 1

    if turn == 1:
        return odd
    elif turn >1:
        return paire
    elif turn == 0:
        return paire
