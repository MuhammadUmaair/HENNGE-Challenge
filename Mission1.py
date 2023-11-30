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
