# Create an empty list
my_list = []

# 1. Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending: ", my_list)

# 2. Insert 15 at the second position
my_list.insert(1, 15)
print("After inserting 15: ", my_list)

# 3. Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending: ", my_list)

# 4. Remove the last element
my_list.pop()
print("After removing last element: ", my_list)

# 5. Sort my_list in ascending order
my_list.sort()
print("After sorting: ", my_list)

# 6. Find and print the index of 30
print("Index of 30: ", my_list.index(30))

# Optional: Print final list for verification
print("\nFinal list: ", my_list)