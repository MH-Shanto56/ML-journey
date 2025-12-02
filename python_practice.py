# 1. Calculate the average of a list
def calculateAvarage(numbers):
    total = sum(numbers)
    avg = total/len(numbers)
    return avg

nums = input("Enter numbers: ")
number_list = list(map(float, nums.split()))

result = calculateAvarage(number_list)
print("The average is: ", result)


#2. Filter even numbers from a list
def filter_even(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even

nums = input("Enter numbers: ")
numbers_list =list(map(int,nums.split()))

even_numbers = filter_even(numbers_list)
print(even_numbers)


#3. Count word frequency in a sentence
