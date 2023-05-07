#!/usr/bin/env python

# List examples
# if you really want to use an array, then use NumPy array, else use list
my_list = [1, 5, 10, 4]

# print(my_list[1])


# list function
# can have different types of items in a list
another_list = list((1, "Bob", 11.5, 4))
print(type(another_list))


# size/length of list
print("Size: " + str(len(another_list)))

# walking through the the list
for item in another_list:
    print(item)


# overriding
another_list[0] = 11

print(another_list)


# removing an item
del another_list[0]
print(len(another_list))
print(another_list)


# more interesting list operations

# append
# O(1)
another_list.append("new item appended")
print(another_list)

# lists are indexed, so might be multiple items with same value
# eg:
another_list.append("new item appended")
print(another_list)

# negative indicies
print("last item:")
print(another_list[-1])

# slicing
print(another_list[0:2])

list1 = [1, 2, 3.5]
list2 = [True, 'list 2', False]


# concatenation
# use the + operator
res_list = list1 + list2
print(res_list)

print(25*"-")
# extend function
list1.extend(list2)
print(list1)
print(list2)


# append
list1.append('david')

# copy
list3 = list1.copy()
print(list3)

# remove
list1.remove(3.5)
print(list1)


# pop
# returns last item appended
pop_result = list1.pop()
print(pop_result)

print(list1)
# reverse
list1.reverse()
print(list1)


# sort
names = ["Joe", "Bob", "Alice", "David"]
print(names)
names.sort()
print(names)

names.reverse()
print(names)


