# Accept user input to create two sets of integers
set1 = set(map(int, input("Enter elements for set 1: ").split()))
set2 = set(map(int, input("Enter elements for set 2: ").split()))

# Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)

# Print the new set
print("Common elements:", common_elements)
