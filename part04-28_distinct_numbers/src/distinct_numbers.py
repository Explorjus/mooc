# Write your solution here
def distinct_numbers(lista):
    # Używamy zbioru, aby usunąć duplikaty
    nowa_lista = list(set(lista))
    # Sortujemy listę
    nowa_lista.sort()
    return nowa_lista

# Testowanie funkcji
if __name__ == "__main__":
    print(distinct_numbers([1, 2, 2, 3, 4, 5, 6, 6]))  # Powinno wydrukować [1, 2, 3, 4, 5, 6]