def histogram(string):
    lista = {}
    for i in string:
        if i in lista:
            lista[i] += 1
        else:
            lista[i] = 1

    for i, count in lista.items():
        print(f"{i} {'*' * count}")


histogram('autkoawsdfsgsdfgbh')

        

        