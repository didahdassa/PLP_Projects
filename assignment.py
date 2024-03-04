my_list = []

my_list.extend([10,20,30,40])

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)

# Print the updated my_list
print("Updated my_list:", my_list)