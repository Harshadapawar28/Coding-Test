# 3. Write a Python function to count the occurrences of a specific element in a list.					

def count_occurrences(lst, element):
  
    return lst.count(element)
my_list = [1, 2, 2, 3, 4, 2, 5, 6]
element_to_count = 2

count = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {count} times in the list.")

# OUTPUT : The element 2 appears 3 times in the list.
