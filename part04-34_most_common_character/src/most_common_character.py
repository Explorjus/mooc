# Write your solution here
def most_common_character(my_string):
    # Konwertujemy wszystkie znaki na małe litery
    my_string = my_string.lower()
    # Znajdujemy najczęściej występujący znak
    return max(my_string, key=my_string.count)

# Testowanie funkcji
if __name__ == "__main__":
    print(most_common_character("Alan Grace Steve Kim Susan"))  # Powinno zwrócić 'a'
    print(most_common_character("aaaa bbb ccc ddddd bbb"))  # Powinno zwrócić 'b'