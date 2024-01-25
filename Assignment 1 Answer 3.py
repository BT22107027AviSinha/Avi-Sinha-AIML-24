lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]

# Accessing the nested list to grab the word "hello", here the nexting is indexed from 0 hence we nest our get() in the 0th term of the second term of the first term of the third term in the list.
hello = lst[3][1][2][0]


print(hello)
