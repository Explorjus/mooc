# Write your solution here

def length_of_longest(lista):
    return max(len(x) for x in lista)

# Testowanie funkcji
if __name__ == "__main__":
    print(length_of_longest(['Alan', 'Grace', 'Steve', 'Kim', 'Susan']))  # Powinno zwrócić 5