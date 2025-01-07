# Write your solution here
def no_shouting(lista):
    # Tworzymy nową listę zawierającą tylko słowa, które nie są w całości napisane wielkimi literami
    nowa = [x for x in lista if not x.isupper()]
    return nowa

# Testowanie funkcji
if __name__ == "__main__":
    print(no_shouting(['Ala', 'ma', 'kota', 'ALE', 'nie', 'ma', 'psa']))  # Powinno wydrukować ['Ala', 'ma', 'kota', 'nie', 'ma', 'psa']
    print(no_shouting(['first', 'Second', 'third', 'fourth', 'fifth']))  # Powinno wydrukować ['first', 'Second', 'third', 'fourth', 'fifth'] 