# Write your solution here
def double_items(numbers):
    numbers_doubled = numbers[:]
    
    for i in range(len(numbers_doubled)):
        numbers_doubled[i] *= 2
    return numbers_doubled

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)