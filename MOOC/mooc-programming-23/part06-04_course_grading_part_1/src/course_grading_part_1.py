# write your solution here

informacja = input('Student information: ')
ukonczone =   input('Exercises completed: ')
dziennik_informacje = {}

with open(informacja) as lista:
    for parts in lista:
        parts = parts.replace("\n", "")
        parts = parts.split(';')
     

        if parts[0] == 'id':
            continue
        imiona = []
        for i in parts[1:]:
            imiona.append(i.strip())
        dziennik_informacje[parts[0]] = imiona
        
   
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

        

for id, name in dziennik_informacje.items():
    if id in dziennik_ukonczone:
        suma_ocen = dziennik_ukonczone[id]
        imie = " ".join(name)
        print(imie, sum(suma_ocen))

