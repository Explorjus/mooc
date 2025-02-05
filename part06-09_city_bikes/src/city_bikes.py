# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    with open(filename) as file:
        slownik = {}
        headers = file.readline().strip().split(';')  # readline wczytuje pierwsza linie z pliku 
        # strip usuwa biale znaki a split tworzy liste z kazdego wyrazu
        
        # Znajdź indeksy odpowiednich kolumn
        name_index = headers.index('name')
        longitude_index = headers.index('Longitude')
        latitude_index = headers.index('Latitude')
        
        for line in file:
            parts = line.strip().split(';')
            name = parts[name_index]
            longitude = float(parts[longitude_index])
            latitude = float(parts[latitude_index])
            slownik[name] = (longitude, latitude)
    
    # Drukowanie wyników w osobnych liniach
    for name, coords in slownik.items():
        print(f"{name}: {coords}")
    
    return slownik

def distance(stations: dict, station1: str, station2: str):
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)




get_station_data('stations1.csv')
stations = get_station_data([0])

distance(stations, station1, station2)


