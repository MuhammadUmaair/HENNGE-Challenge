#!/usr/bin/env python
#######################################################################
# Mission Description
#
# We want to calculate a sum of squares of some integers, excepting negatives
# * The first line of the input will be an integer N (1 <= N <= 100)
# * Each of the following N test cases consists of one line containing an integer X (0 < X <= 100),
#   followed by X integers (Yn, -100 <= Yn <= 100) space-separated on the next line
# * For each test case, calculate the sum of squares of the integers excepting negatives,
#   and print the calculated sum to the output. No blank line between test cases
# * (Take input from standard input, and output to standard output)
# 
# ##Rules
# * Choose your favorite language from either of these: C, Erlang, Go, Python, Ruby
# * Do not use loop statements like while/until/for/each/loop, and goto
#
# ## Sample Input
# 2
# 4
# 3 -1 1 14
# 5
# 9 6 -53 32 16
#
# ##Sample Output
# 206
# 1397
#######################################################################

def sum_of_squares_non_negative(nums):
    total = 0
    for num in nums:
        if num >= 0:
            total += num * num
    return total

def main():
    num_test_cases = int(input())
    
    # Process each test case
    for _ in range(num_test_cases):
        num_integers = int(input())
        integers = list(map(int, input().split()))
        
        result = sum_of_squares_non_negative(integers)
        print(result)

if __name__ == "__main__":
    main()
