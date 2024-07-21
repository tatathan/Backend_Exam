"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:
    def find_tailing_zeroes_in_factorial(self, number: int) -> int | str:
        factorial_value = self.find_factorial(number)
        if isinstance(factorial_value, int):
            # print(f"factorial: {factorial_value}")
            zero_count = self.find_tailing_zeroes(factorial_value)
            return zero_count
        else:
            return factorial_value

    def find_tailing_zeroes(self, number: int) -> int:
        zero_count = 0
        while number % 10 == 0:
            zero_count += 1
            number //= 10
        return zero_count
        

    def find_factorial(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        if number == 0:
            return 1
        
        factorial_value = 1
        for i in range(1, number+1):
            factorial_value *= i
        return factorial_value


while True:
    print("")
    print("Type 'exit' to stop running.")
    number = input("input number: ")
    if number == 'exit':
        break
    try:
        solution = Solution()
        result = solution.find_tailing_zeroes_in_factorial(int(number))
        print(f"count: {result}")
    except ValueError:
        print("count: Input must be integer.")