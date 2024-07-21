"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:

        def ones(number):
            return number_in_thai[number]
        
        def tens(number):
            # tens place
            tens_place = number // 10
            tens_in_thai = number_in_thai.copy()
            tens_in_thai[1] = ""
            tens_in_thai[2] = "ยี่"
            # ones place
            ones_place = number % 10
            ones_in_thai = number_in_thai.copy()
            ones_in_thai[1] = "เอ็ด"
            return f"{tens_in_thai[tens_place]}สิบ{ones_in_thai[ones_place]}"
        
        def below_100(number):
            if number < 10:
                return ones(number)
            elif number < 100:
                return tens(number)
        
        max_value = 10000000
        if number < 0:
            return "number can not less than 0"
        elif number > max_value:
            return "number can not more than 10,000,000"
        elif number == 0:
            return "ศูนย์"
        else:
            number_in_thai = {
                0: "",
                1: "หนึ่ง",
                2: "สอง",
                3: "สาม",
                4: "สี่",
                5: "ห้า",
                6: "หก",
                7: "เจ็ด",
                8: "แปด",
                9: "เก้า"
            }

            num_text = ""
            # millions_place
            millions_place = number // 1000000
            if millions_place:
                if millions_place == 10:
                    num_text = "สิบล้าน"
                else:
                    num_text = num_text + number_in_thai[millions_place] + "ล้าน"
            # hundred_thousands_place
            hundred_thousands_place = (number // 100000) % 10
            if hundred_thousands_place:
                num_text = num_text + number_in_thai[hundred_thousands_place] + "แสน"
            # ten_thousands_place
            ten_thousands_place = (number // 10000) % 10
            if ten_thousands_place:
                num_text = num_text + number_in_thai[ten_thousands_place] + "หมื่น"
            # ten_thousands_place
            thousands_place = (number // 1000) % 10
            if thousands_place:
                num_text = num_text + number_in_thai[thousands_place] + "พัน"
            # hundreds_place
            hundreds_place = (number // 100) % 10
            if hundreds_place:
                num_text = num_text + number_in_thai[hundreds_place] + "ร้อย"
            # tens and ones place
            num_text = num_text + below_100(number % 100) 

            return num_text              
        
while True:
    print("")
    print("Type 'exit' to stop running.")
    number = input("input number: ")
    if number == 'exit':
        break
    try:
        solution = Solution()
        result = solution.number_to_thai(int(number))
        print(f"num_text: {result}")
    except ValueError:
        print("num_text: Input must be integer.")
