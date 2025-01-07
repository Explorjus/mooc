# Write your solution here
def shortest(lista):
    # Znajdujemy najkrótsze słowo
    najkrotsze_slowo = min(lista, key=len)
    return najkrotsze_slowo

# Testowanie funkcji
if __name__ == "__main__":
    print(shortest(['Alan', 'Steve', 'maerek']))  # Powinno wydrukować 'Alan'
    print(shortest(['Alan', 'Susan', 'Seymour', 'Kim', 'Susan']))  # Powinno wydrukować 'Kim'