# Write your solution here
def invert(s):
    nowa = {}
    
    for klucz, wartosc in s.items():  #iteruje przez klucz i warotsc w slowniku s 
        nowa[wartosc] = klucz    #zamineia miejscami klucz i wartosc
    
    s.clear()       #czysci oryginalny slownik
    s.update(nowa)  #dodaje odwrocone pary do oryginalenj listy
    
    print(nowa)



if __name__ == "__main__":  
    s = {1: 10, 2: 20, 3: 30}
    invert(s)
   