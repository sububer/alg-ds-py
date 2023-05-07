#!/usr/bin/env python

# "A palindrome is a string that reads the same forward and backward"

# For example: radar or madam

# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not! 



def is_palindrome_one(s):
    
    # empty and single char strings are palindromes
    if len(s) <= 1:
        return True
    else:
        # walk the string from both ends, comparing the chars
        low_char_idx = 0
        high_char_idx = len(s) - 1

        while low_char_idx < high_char_idx:
            if s[low_char_idx] != s[high_char_idx]:
                return False
            else:
                # advance low_char_idx, decrement high_char_idx
                low_char_idx += 1
                high_char_idx -= 1
            
        # if we get here, then the string is a palindrome
        return True



if __name__ == "__main__":
    # test cases
    s = "radar"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = ""
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = "x"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = "ab"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = "dd"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = "aba"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = "abb"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = "abba"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))

    s = "abcd"
    print("original string: " + s)
    print("is_palindrome_one: " + str(is_palindrome_one(s)))