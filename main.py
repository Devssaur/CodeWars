#https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
def digital_root(n):
    tmp = str(n)
    if len(tmp) <=1:
        return int(tmp)
    else:
        array_string = list(tmp)
        valor = 0

        for i in array_string:
            valor += int(i)
        return digital_root(valor)


print(digital_root(150))
