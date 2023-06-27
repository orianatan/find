Implement a program to find the largest and smallest numbers in a given list:
python
Copy code
def find_min_max(numbers):
    if len(numbers) == 0:
        return None

    min_num = max_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return min_num, max_num

input_list = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in input_list.split()]
min_number, max_number = find_min_max(numbers)

if min_number is None:
    print("The list is empty.")
else:
    print("Smallest number:", min_number)
    print("Largest number:", max_number)
