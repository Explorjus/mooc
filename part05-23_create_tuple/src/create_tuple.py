# Write your solution here
def create_tuple(x: int, y: int, z: int):
    lista = ['','','']
    
    lista[0] = x
    lista[1] = y
    lista[2] = z 
    najm = min(lista)
    najw = max(lista)
    najm = min(lista)
    najw = max(lista)
   
    lista[2] = (x + y + z)

  
   
    lista[0] = najm
    lista[1] = najw
    nowa = tuple(lista)
    return nowa


if __name__ == "__main__":
    print(create_tuple(1, 4, 2))