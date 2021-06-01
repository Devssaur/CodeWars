def find_outlier(integers):
    for item in len(integers):
      if item %2 == 0:
         return item

find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])