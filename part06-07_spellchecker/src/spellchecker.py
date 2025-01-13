# write your solution here


tekst = input("Write text: ")

with open('wordlist.txt', 'r') as slowa:
    slowa_set = set(slowa.read().lower().split())

wynik = []

for wyraz in tekst.split():
    if wyraz.lower() in slowa_set:
        wynik.append(wyraz)
    else:
        wynik.append(f"*{wyraz}*")

print(" ".join(wynik))