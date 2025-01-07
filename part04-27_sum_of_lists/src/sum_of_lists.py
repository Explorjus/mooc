# Write your solution here
def list_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]

# Testowanie funkcji
if __name__ == "__main__":
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(list_sum(list1, list2))  # Powinno wydrukować [5, 7, 9]