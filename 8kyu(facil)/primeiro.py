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

    # print(pair)
    # print(odd)
    # print(turn)
    # elif item >0 and item%2 == 1:
    # print(item)
    # if(sum(integers)%2 == 0):
    #     for item in list(integers):
    #         if item %2 == 1 and item >0:
    #             vowel = item
    #             return vowel
    # elif (sum(integers)%2 == 1):
    #     for item in list(integers):
    #         if item %2 == 1 and item >0:
    #             vowel = item
    #             return vowel


#print(find_outlier([2, 4, 0, 100, 41, 12, 2602, 36]))
#print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
# print(find_outlier(
#     [1924333, 1427953, -246637000, -3163435, -1607979, -549487, 8825201, -5756237, -6125133, -374537, 6123590, 5956679,
#      -5499657, -766027, 942705, 2479167, -5031353, 2499509, 5604361, -9270911, -1085459, 2813859, 3335345, -807169,
#      -1570225, 4085383, 1344229, -3802975, 5168677, 7473749, 8026015, 1822153, 7760925, -8467837, -7926265, 4488461,
#      -2019153, 3846477, -34095, -3939741, 9964263, 5395167, -2131673, 2254127]))








