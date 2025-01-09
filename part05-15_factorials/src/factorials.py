def factorials(n: int):
    result = {}    #tworzy slownik
    factorial = 1   #zmienna przehowujaca warotos silni
    for i in range(1, n + 1):    #petla for w zakresie 1 do n 
        factorial *= i           #oblicza silnię mnożąc przez kolejne liczby
        result[i] = factorial    #dodanie wyniku silni do dziennika 
    return result    #zwort slownik z wynikami silni





if __name__ == "__main__":
    k = factorials(5)
    print(factorials(5))
    print(k[3])

