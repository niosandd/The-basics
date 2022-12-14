nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

flat = [num for row in nice_list for row_i in row for num in row_i]
print(flat)