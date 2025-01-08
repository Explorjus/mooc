# Write your solution here
def longest(strings: list):
    # Znajdujemy najdłuższy ciąg znaków używając klucza `key=len`
    najdluzszy = max(strings, key=len)
    return najdluzszy

# Testowanie funkcji
if __name__ == "__main__":
    print(longest(['maria', 'ania']))  # Powinno wydrukować 'maria'