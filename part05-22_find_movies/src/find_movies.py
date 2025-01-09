# Write your solution here
def find_movies(database: list, name: str):
    nowa = []  #tworzy nowa liste
    for film in database:   #iteruje 'film' przez baze danych
        if name.lower() in film["name"].lower():  #sprawdzenie czy tytul znajduje sie sie w bazie danych
            nowa.append(film) #dodaje do nowej listy liste w kotrej znajduje sie tytul zawierajacy podany wyraz
            
    return nowa

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "Python")
    print(my_movies)
