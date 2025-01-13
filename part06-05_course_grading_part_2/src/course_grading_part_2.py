# wwite your solution here
informacja = input('Student information: ')
ukonczone =   input('Exercises completed: ')
punkty = input('Exam ponits: ')

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




sum_ocen = {}

with open(punkty) as lista_punkty:
    for oceny in lista_punkty:
        oceny = oceny.replace('\n', '')
        oceny = oceny.split(';')
        if oceny[0] == 'id':
            continue
        
        lista_ocen = []
        for x in oceny[1:]:
                lista_ocen.append(int(x))
        sum_ocen[oceny[0]] = sum(lista_ocen)
   

suma = {}

for id, name in dziennik_informacje.items():  #iteruje przez wszytykie lementy id to klucz a name to imie i nazwisko
    if id in dziennik_ukonczone:   #jesli id jest w dzie._ukon. 
        oceny = dziennik_ukonczone[id]    #pobiera liste ocen dla danego studenta i przypisuje do do zmiennej oceny 
        imie = " ".join(name) #łączy elementy lsity name w jeden ciag znakow
        suma[id] = sum(oceny)
        #print(imie, sum(oceny))  #drukuje pelne imie i nazwisko oraz sume jego ocen
#print(suma)
        
suma1 = {}    
for id, name in dziennik_informacje.items():
        if id in sum_ocen:
            oceny = sum_ocen[id]
            imie = ' '.join(name)    
            suma1[id] = oceny   
                
        #print(imie, (oceny)) 
#print(suma1)

last = {}
for id, oceny in suma.items():
    if id in suma1:
        exercise_points = suma[id] // 4  # Przeliczanie punktów z ćwiczeń na skalę 0-10
        total_points = exercise_points + suma1[id]  # Suma punktów z ćwiczeń i egzaminu
        last[id] = total_points

        
for id in last:
    if last[id] >= 0 and last[id] <= 14:
        last[id] = 0
    elif last[id] >= 15 and last[id] <= 17:
        last[id] = 1
    elif last[id] >= 18 and last[id] <= 20:
        last[id] = 2
    elif last[id] >= 21 and last[id] <= 23:
        last[id] = 3
    elif last[id] >= 24 and last[id] <= 27:
        last[id] = 4
    elif last[id] >= 28:
        last[id] = 5

for id, name in dziennik_informacje.items():
        if id in last:
            imie = ' '.join(name)
            print(imie, last[id])

