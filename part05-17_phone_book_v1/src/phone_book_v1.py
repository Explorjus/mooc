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
       
        ksiazka[imie] = numer
        print("ok!")
        
    elif komenda == 1:
        imie = input("name: ")
        if imie in ksiazka:
            print(ksiazka[imie])
        else:
            print("no number")
            





