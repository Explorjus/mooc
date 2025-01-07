# Write your solution here
def longest_series_of_neighbours(lista):
    if not lista:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(lista)):
        if abs(lista[i] - lista[i - 1]) == 1:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length

# Testowanie funkcji
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))  # Powinno wydrukować 4