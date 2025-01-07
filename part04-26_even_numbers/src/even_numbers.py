# Write your solution here
def even_numbers(lista):
    even_lista = [x for x in lista if x % 2 == 0]
    return even_lista

# Testowanie funkcji
if __name__ == "__main__":
    print(even_numbers([1, 4, 6]))  # Powinno wydrukować [4, 6]
