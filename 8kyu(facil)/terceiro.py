#https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python/60b5ad0408092600253ecba7

#def get_count(input_str):
#    num_vowels = 0
 #   for item in list(input_str):
  #      if item == 'a' or  item == 'e' or  item == 'i' or  item == 'o' or  item == 'u' :
   #         num_vowels += 1

    #return num_vowels

#print(get_count("eit"))

def getCount(inputStr):
    soma = print(sum(1 for let in inputStr if let in "aeiouAEIOU"))
    return soma

print(getCount("gUilherme"))

