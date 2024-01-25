list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# Find the inner list containing 6000
inner_list = list1[2][2]

# Find the index of 6000 in the inner list
index_6000 = inner_list.index(6000)

# Insert 7000 after 6000
inner_list.insert(index_6000 + 1, 7000)

print(list1)
