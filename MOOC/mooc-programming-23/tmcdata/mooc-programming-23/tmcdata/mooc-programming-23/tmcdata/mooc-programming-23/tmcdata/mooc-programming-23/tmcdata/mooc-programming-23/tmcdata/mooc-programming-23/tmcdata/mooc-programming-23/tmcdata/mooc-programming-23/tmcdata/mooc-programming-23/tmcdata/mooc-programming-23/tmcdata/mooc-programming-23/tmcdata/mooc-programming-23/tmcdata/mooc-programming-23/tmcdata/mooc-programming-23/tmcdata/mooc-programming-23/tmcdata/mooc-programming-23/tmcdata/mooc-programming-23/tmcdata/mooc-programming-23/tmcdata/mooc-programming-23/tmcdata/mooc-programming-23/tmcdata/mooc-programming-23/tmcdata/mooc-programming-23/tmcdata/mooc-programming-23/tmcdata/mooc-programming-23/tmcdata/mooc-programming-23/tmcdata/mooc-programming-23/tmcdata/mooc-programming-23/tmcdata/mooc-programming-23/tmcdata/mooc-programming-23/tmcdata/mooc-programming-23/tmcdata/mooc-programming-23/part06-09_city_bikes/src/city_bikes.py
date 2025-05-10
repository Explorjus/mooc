# tee ratkaisu tänne
# Write your solution here
import math 

def get_station_data(filename: str):
    with open(filename, 'r') as file:
        stacje = {}
        headers = file.readline().strip().split(';')  # Wczytuje nagłówki kolumn 
        
        # Znajdź indeksy odpowiednich kolumn
        longitude_index = headers.index('Longitude') #indeks szerokości 
        latitude_index = headers.index('Latitude') #indeks długości 
        name_index = headers.index('name')  #nazwa miasta
        
        for line in file:   #iteruje przez kazda linie w pliku zaczynajac od drugiej lini poniewaz pierwsza zsotala wczytana
            parts = line.strip().split(';')   # jako headers
            name = parts[name_index]   
            longitude = float(parts[longitude_index])
            latitude = float(parts[latitude_index])
            stacje[name] = (longitude, latitude)
    
    return stacje

def distance(stations: dict, station1: str, station2: str):
    
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]
    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    station1 = ""
    station2 = ""
    
    station_names = list(stations.keys())  #tworzy liste z kluczami słownika
    for i in range(len(station_names)): #iteruje przez indeksy station_names od 0 
        for j in range(i + 1, len(station_names)):  #iteruje przez indeksy od i + 1. iteracje są po to aby nie powtórzyć porównania stacji
            s1 = station_names[i] # przechowuje nazwe stacji z pierwszej pętli
            s2 = station_names[j] # robi to samo ale z drugiej pętli
            dist = distance(stations, s1, s2)  # oblicza dystans między tymi stacjami za pomomocą funcji distance
            if dist > max_distance: # jeśli obliczony dystans jest większy od wcześniejszego jest nadpisywanyt
                max_distance = dist
                station1 = s1
                station2 = s2
    
    return (station1, station2, max_distance)


if __name__ == "__main__":

    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

# Przykładowe wywołanie funkcji
    stations = get_station_data("stations1.csv")
    for name, coords in stations.items():
        print(f"{name}: {coords}")

   

 