# Write your solution here
def histogram(string):
    lista = {}
    
    for char in string:
        if char in lista:
            lista[char] += 1
        else:
            lista[char] = 1

    

    for char, count in lista.items():
        print(f"{char} {'*' * count}")

if __name__ == "__main__":
    
    histogram("statistically")