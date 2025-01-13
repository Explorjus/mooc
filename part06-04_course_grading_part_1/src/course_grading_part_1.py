# write your solution here

informacja = input('Student information: ')
ukonczone =   input('Exercises completed: ')
dziennik_informacje = {}

with open(informacja) as lista: #otwiera plik
    for parts in lista:  #iteruje przez kazdy elemennt w otwrtym pliku
        parts = parts.replace("\n", "")  #zamienia \n na puste miejsce 
        parts = parts.split(';') #dzieli wyrazy kiedy przy iteracji będzie ;
     

        if parts[0] == 'id':  #pomija nagłówk aby nie doodać go do bazy
            continue
        imiona = [] #tworzy nową liste na imiona
        for i in parts[1:]:  #iteruje przez kady elemety w parts zaczynają od drugiego do końca listy
            imiona.append(i.strip()) #dodaje imiona do listy 
        dziennik_informacje[parts[0]] = imiona #dodaje liste inioma do slownika przypisując do niego klucz któy znajduje sie na począktu listy
        
   
dziennik_ukonczone = {}

with open(ukonczone) as lista:
    for parts in lista:
        parts = parts.replace("\n", "")
        parts = parts.split(';')
        if parts[0] == 'id':
            continue

        oceny = []   #tworzy pusta liste
        for x in parts[1:]:     #iteruje przez elementy zaczynajac od drugiego do końca 
            oceny.append(int(x))   #dodaje do listy wartosc jako int
        dziennik_ukonczone[parts[0]] = oceny    #dodaje do słownika listy o takim samym kluczu

        

for id, name in dziennik_informacje.items():  #iteruje przez wszytykie lementy id to klucz a name to imie i nazwisko
    if id in dziennik_ukonczone:   #jesli id jest w dzie._ukon. 
        oceny = dziennik_ukonczone[id]    #pobiera liste ocen dla danego studenta i przypisuje do do zmiennej oceny 
        imie = " ".join(name) #łączy elementy lsity name w jeden ciag znakow
        print(imie, sum(oceny)) #drukuje pelne imie i nazwisko oraz sume jego ocen

