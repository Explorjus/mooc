def read_fruits():
    lista = {}
    with open("fruits.csv") as lista_owocow:
        for linia in lista_owocow:
            linia = linia.strip()  
            nazwa, cena = linia.split(';')  
            lista[nazwa] = float(cena)  


    return lista


if __name__ == "__main__":
    print(read_fruits())