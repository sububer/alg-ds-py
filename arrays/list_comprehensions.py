#!/usr/bin/env python

# list comprehensions
# https://docs.python.org/3.11/tutorial/datastructures.html#list-comprehensions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = []


# using list comprehensions
# filter on even numbers
new_list = [num for num in numbers if num % 2 == 0]

print(new_list)


names = ["Bob", "Alice", "John", "Mary", "Joe", "Jane"]

# filter on names that start with J

names_with_j = [name for name in names if name.startswith("J")]
print(names_with_j)