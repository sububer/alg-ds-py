#!/usr/bin/env python

# Integer reversion exercise
# Your task is to design an efficient algorithm to reverse a given integer. For example if the input of the algorithm is 1234 then the output should be 4321.

# NOTE: the input is an integer (and not a string) !!!



def reverse_integer(n):
    # num is the integer to reverse

    # convert num to a list of chars
    num_str_list = list(str(n))

    # do the usual reversal

    size = len(num_str_list)
    low_idx = 0
    high_idx = size - 1

    while low_idx < high_idx:
        # swap
        tmp = num_str_list[low_idx]
        num_str_list[low_idx] = num_str_list[high_idx]
        num_str_list[high_idx] = tmp

        # advance low_idx, decrement high_idx
        low_idx += 1
        high_idx -= 1

    # convert num_str back to an integer
    return int("".join(num_str_list))


def reverse_integer_two(n):
    # num is the integer to reverse
    # build up the reversed number by multiplying by 10 and adding the next digit

    n_str = str(n)
    size = len(n_str)
    magnitude = size - 1

    if magnitude == 0:
        return n
    
    else:
        reversed_num = 0

        while magnitude >= 0:
            reversed_num += int(n_str[magnitude]) * 10 ** magnitude
            magnitude -= 1

        return reversed_num


if __name__ == "__main__":
    print("reverse_integer(1234): " + str(reverse_integer(1234)))
    print("reverse_integer(1): " + str(reverse_integer(1)))
    print("reverse_integer(12): " + str(reverse_integer(12)))


    print("reverse_integer_two(1234): " + str(reverse_integer_two(1234)))
    print("reverse_integer_two(1): " + str(reverse_integer_two(1)))
    print("reverse_integer_two(12): " + str(reverse_integer_two(12)))
    print("reverse_integer_two(6789): " + str(reverse_integer_two(6789)))
    print("reverse_integer_two(0): " + str(reverse_integer_two(0)))
    print("reverse_integer_two(80): " + str(reverse_integer_two(80)))
    