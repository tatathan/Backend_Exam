"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if not (0 < number < 4000):
            return "Number must be between 1 and 3999"
        number_range = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5 ,4 ,1]
        symbols = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        roman_numb = ""
        for value in number_range:
            multiple = number // value
            if multiple != 0:
                roman_numb = roman_numb + multiple*symbols[value]
                number = number - multiple*value
                if number == 0:
                    return roman_numb
                

while True:
    print("")
    print("Type 'exit' to stop running.")
    number = input("input number: ")
    if number == 'exit':
        break
    try:
        solution = Solution()
        result = solution.number_to_roman(int(number))
        print(f"roman_text: {result}")
    except ValueError:
        print("roman_text: Input must be integer.")