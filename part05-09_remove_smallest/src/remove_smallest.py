# usunac najmniejsza liczbe i zodyfikowac przy tum lsiste
def remove_smallest(numbers):
    lista_najmniejsa = min(numbers)
    numbers.remove(lista_najmniejsa)

            

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)