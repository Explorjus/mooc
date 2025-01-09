# Write your solution here
ksiazka = {}
while True:
    komenda = int(input("command (1 search, 2 add, 3 quit) "))
        
    if komenda == 3:
        print("quitting...")
        break
        
    elif komenda == 2:
        imie = input("name: ") 
        numer = input("number: ")
        if imie not in ksiazka:   #sprawdza czy imie znajduje sie w ksizace 
            ksiazka[imie] = []    #jesli nie, tworzy liste przy imieniu w celu dodania kolejcnej warotsci
        ksiazka[imie].append(numer)   #dodaje numer do imienia 
        print("ok!")
        
    elif komenda == 1:
        imie = input("name: ")
        if imie in ksiazka:   #jesli imie jest w ksiazce 
            for numer in ksiazka[imie]:  #iteruje przez listę numerów przypisaną do klucza imie w słowniku ksiazka
                print(numer)
        else:
            print("no number")