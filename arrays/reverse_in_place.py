#!/usr/bin/env python

# In this exercise, you have to reverse a list in O(N) linear time complexity and we want the algorithm to be in-place as well - so the algorithm can not use additional memory (it means you have to manipulate the input list and not create an independent list)!

# For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

# Good luck!


def reverse_in_place_one(nums):
    # nums is the list containing the numbers
    # write your code here

    # size of the list
    size = len(nums)

    # nothing to swap if list is empty or has only one element
    if size <= 1:
        return nums
    else:
        # list size is >= 2.. do the swapping
        num_swapped = 0
        head = 0
        tmp_swap_val = 0
        while num_swapped < size / 2:
            # tail position is calculated relative to head position
            tail = size - 1 - head
            tmp_swap_val = nums[head]
            nums[head] = nums[tail]
            nums[tail] = tmp_swap_val
            # advance head, increment num_swapped
            head += 1
            num_swapped += 1


def reverse_in_place_two(nums):
    # nums is the list containing the numbers

    # size of the list
    size = len(nums)

    # nothing to swap if list is empty or has only one element
    if size <= 1:
        return nums
    else:
        # list size is >= 2.. do the swapping
        # keep track of indices, low and high
        low_idx = 0
        high_idx = size - 1

        while (low_idx < high_idx):
            # swap
            tmp_swap_val = nums[low_idx]
            nums[low_idx] = nums[high_idx]
            nums[high_idx] = tmp_swap_val

            # advance low_idx, decrement high_idx
            low_idx += 1
            high_idx -= 1




if __name__ == "__main__":

    # test cases
    # empty list
    nums = []
    print("Original list: ", nums)
    reverse_in_place_two(nums)
    print("Reversed list: ", nums)

    # single item list
    nums = [1]
    print("Original list: ", nums)
    reverse_in_place_two(nums)
    print("Reversed list: ", nums)


    # two element list
    nums = [1, 2]
    print("Original list: ", nums)
    reverse_in_place_two(nums)
    print("Reversed list: ", nums)


    # three element list
    nums = [1, 2, 3]
    print("Original list: ", nums)
    reverse_in_place_two(nums)
    print("Reversed list: ", nums)

    # odd number of elements
    nums = [1, 2, 3, 4, 5, 6, 7]
    print("Original list: ", nums)
    reverse_in_place_two(nums)
    print("Reversed list: ", nums)


    # even number of elements
    nums = [1, 2, 3, 4]
    print("Original list: ", nums)
    reverse_in_place_two(nums)
    print("Reversed list: ", nums)

    # even number of elements
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print("Original list: ", nums)
    reverse_in_place_two(nums)
    print("Reversed list: ", nums)

