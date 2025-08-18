# Create an empty list
my_list = []

# Add (append) numbers one by one
my_list.append(10)   # list becomes [10]
my_list.append(20)   # list becomes [10, 20]
my_list.append(30)   # list becomes [10, 20, 30]
my_list.append(40)   # list becomes [10, 20, 30, 40]

# Insert 15 at the second position (index 1, since counting starts from 0)
my_list.insert(1, 15)  # list becomes [10, 15, 20, 30, 40]

# Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])  # list becomes [10, 15, 20, 30, 40, 50, 60, 70]

# Remove the last element from the list
my_list.pop()  # removes 70 → list becomes [10, 15, 20, 30, 40, 50, 60]

# Sort the list in ascending order
my_list.sort()  # already in order, so list stays [10, 15, 20, 30, 40, 50, 60]

# Find and print the index (position) of number 30
index_of_30 = my_list.index(30)

# Final output
print("Final List:", my_list)
print("Index of 30 is:", index_of_30)