# Write your solution here
def times_ten(start_index: int, end_index: int):
    dziennik = {}
    i = start_index 
    for i in range(start_index, end_index + 1):
       a = i*10
       dziennik[i] = a

       

    return dziennik
       

if __name__ == "__main__":
 print(times_ten(1, 6))