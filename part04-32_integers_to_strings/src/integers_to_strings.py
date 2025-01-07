# Write your solution here
def formated_numbers(lista):
    nowa = [f"{x:.2f}" for x in lista]
    return nowa

# Testowanie funkcji
if __name__ == "__main__":
    formated_numbers([1, 2, 3, 4, 5])
    now_lista=formated_numbers()
    print(now_lista)  # Powinno wydrukować ['1.00', '2.00', '3.00', '4.00', '5.00']