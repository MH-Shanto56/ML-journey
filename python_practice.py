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
def word_frequency(sentence):
    words = sentence.split() #splitting the sentence ["I", "love", "python", "I", "love", "coding"]
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

sentence = input("Enter a sentence: ")
print(word_frequency(sentence))


#4. Reverse a string
def reverse(text):
    string=text[::-1]
    return string

name = input("Enter your name: ")
rev = reverse(name)
print(rev)


#5. Find the max value in a dictionary
def max_in_dict(dict):
    return max(dict.values())

dict = {}
n = int(input("how many items do you want: "))

for i in range(n):
    key = input("enter item: ")
    value = input("enter value: ")
    dict[key] = value

max_value = max_in_dict(dict)
print(max_value)
