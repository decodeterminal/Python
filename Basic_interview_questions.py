# Q1: Reverse a string without using text[::-1] or built-in functions.
# 
# Input: "cybersecurity"
# Expected Output: "ytirucesrebyc"

a = "cybersecurity"
reverse_string = ""
for char in a:
    reverse_string = char + reverse_string
print(reverse_string)



























# Q2: Loop from numbers 1 to 50. 
#     - If divisible by 3, print "Fizz"
#     - If divisible by 5, print "Buzz"
#     - If divisible by both 3 and 5, print "FizzBuzz"
#     - Otherwise, print the number.


for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)




























#Q3: Check if a word reads the same backward as forward. 
#     Do not use any built-in reverse functions.
# 
# Input: "malayalam" -> Expected Output: True
# Input: "network"   -> Expected Output: False


word = "malayalam"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break
print(is_palindrome)



















#Q4: Given a list of numbers, find the highest and lowest values
#     without using Python's built-in max() or min() functions.
# 
# Input: [42, 17, 93, 8, 55, 21]
# Expected Output: Max is 93, Min is 8




numbers = [42, 17, 93, 8, 55, 21]
max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print(f"Max is {max_num}, Min is {min_num}")

















# Q5: Given a list containing duplicate elements, return a new list
#     with only the unique elements. Do not use set().
# 
# Input: [5, 2, 9, 2, 5, 3, 1, 9]
# Expected Output: [5, 2, 9, 3, 1]

input_list = [5, 2, 9, 2, 5, 3, 1, 9]
unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list) 