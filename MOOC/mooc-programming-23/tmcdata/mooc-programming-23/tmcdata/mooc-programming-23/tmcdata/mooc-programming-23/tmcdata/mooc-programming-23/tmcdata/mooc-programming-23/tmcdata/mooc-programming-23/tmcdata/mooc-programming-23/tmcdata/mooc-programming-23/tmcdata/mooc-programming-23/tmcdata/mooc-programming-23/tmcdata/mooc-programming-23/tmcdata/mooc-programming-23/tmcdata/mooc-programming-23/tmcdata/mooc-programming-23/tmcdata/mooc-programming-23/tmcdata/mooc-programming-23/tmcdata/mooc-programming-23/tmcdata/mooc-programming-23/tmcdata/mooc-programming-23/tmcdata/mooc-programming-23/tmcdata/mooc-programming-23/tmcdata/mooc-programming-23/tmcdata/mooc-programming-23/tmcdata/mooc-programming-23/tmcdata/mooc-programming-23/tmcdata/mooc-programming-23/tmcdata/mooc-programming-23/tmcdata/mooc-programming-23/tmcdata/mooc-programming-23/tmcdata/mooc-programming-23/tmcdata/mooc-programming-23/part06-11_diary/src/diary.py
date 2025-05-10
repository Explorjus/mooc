# Write your solution here
print("1 - add an entry, 2 - read entries, 0 - quit")

while True:
    funkcja = int(input("Fuction: "))

    if funkcja == 1:
        wejscie = input("Diary entry: ")

        with open("diary.txt", "a") as myfile:
            myfile.write(wejscie + "\n")

        print("Diary saved")

    elif funkcja == 2:
        with open("diary.txt", "r") as myfile:
            plik = myfile.read()
            print(plik)

    elif funkcja == 0:
        print("Bye now!")
        break

              