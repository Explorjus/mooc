# write your solution here
def matrix_max():
    lista = lista_calkowita()
    najw = max(max(i) for i in lista)
    print(najw)
    return najw

def row_sums():
    lista = lista_calkowita()
    nowa = [sum(row) for row in lista]  # Oblicza sumę każdego rzędu i tworzy nową listę
    for i, suma in enumerate(nowa, start=1):
        print(f"{i}, {suma}")
    return nowa

def matrix_sum():
    lista = lista_calkowita()
    suma = sum(sum(row) for row in lista)  # Sumuje wszystkie liczby w macierzy
    print(suma)
    return suma

def lista_calkowita():
    with open('matrix.txt') as lista_liczb:
        lista = []
        for liczby in lista_liczb:
            liczby = liczby.strip()
            liczby = liczby.split(',')
            liczby = [int(x) for x in liczby]
            lista.append(liczby)
    return lista

if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()