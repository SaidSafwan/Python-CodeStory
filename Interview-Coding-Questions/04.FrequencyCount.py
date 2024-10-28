# Question: Write a Python program to count the frequency of each element in a list.

num = [1, 2, 3, 1, 3, 4, 2, 2, 3, 5]

def countFrequency(numbers):
    freq = {} #empty dictionary
    for num in numbers:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

freq_count = countFrequency(num)
print(freq_count)

