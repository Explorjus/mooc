# Write your solution here
def everything_reversed(lista):
    nowa = [i[::-1] for i in lista[::-1]]
    return nowa
 
if __name__ == "__main__":
    nowa_lista = everything_reversed(['avc']) # Powinno wydrukować [5, 4, 3, 2, 1]
 