# write your solution here



def largest():
    with open("numbers.txt") as plik:
        lista = []

        for liczby in plik:
            liczby = liczby.replace("\n", "")
            jakoint =int(liczby)
            lista.append(jakoint)
    
        najw = max(lista)
        return najw

if __name__ == "__main__":
    print(largest())