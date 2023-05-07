#!/usr/bin/env python

# Anagram checker exercise

def is_anagram(str1, str2):

    # your algorithm goes here
    # return True if str1 and str2 are anagrams, otherwise return False

    if len(str1) != len(str2):
        return False

    # convert strings to lists
    str1_list = list(str1)
    str2_list = list(str2)

    # sort the lists
    return (sorted(str1_list) == sorted(str2_list))



