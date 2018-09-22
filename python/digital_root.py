#!/usr/bin/env python3


def digital_root(num):
    test_sum = 0
    nums = [n for n in str(num)]
    for n in nums:
        test_sum += int(n)
    if len(str(test_sum)) > 1:
        digital_root(test_sum)
    else:
        print(test_sum)


# Tests
digital_root(123) # 6
digital_root(453) # 3
digital_root(7394) # 5
digital_root(16) # 7
digital_root(456) # 6
digital_root(123456789) # 9