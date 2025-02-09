def read_fruits():
    lista = {}
    with open("fruits.csv") as lista_owocow:
        for linia in lista_owocow:
            linia = linia.strip()  # Usuwa znaki nowej linii i białe znaki
            nazwa, cena = linia.split(';')  # Rozdziela nazwę owocu i cenę
            lista[nazwa] = float(cena)  # Dodaje do słownika z ceną jako float

    return lista


if __name__ == "__main__":
    print(read_fruits())