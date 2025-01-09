def add_student(students, name):
    if name not in students:     # sprawdza czy studenta nie ma juz na liscie
        students[name] = []     # jesli nie tworzy go i puste miejsce zaraz obok



def print_student(students, name):
    liczba_kursow = 0
    suma = 0
    if name in students:    # sprawdza czy student jest w bazie danych
        print(f"{name}:")   
        
        if students[name] == []:    # jesli student ma puste pole to znaczy nie unoczyl zadnego kursu
            print(" no completed courses")
        else:
            for kurs in students[name]:
                liczba_kursow += 1
            
            print(f" {liczba_kursow} completed courses: ")

            
            for kurs in students[name]: # iteruje przez kursy w liscie przypisanej do studenta
                
                print(f"  {kurs[0]} {kurs[1]}")  # printuje kursy ktore sa zpaisane w tuple
                suma += kurs[1]
            
            for kurs in students[name]:
                if kurs[0] in students[name]:
                    students[kurs[1]] = 0
           
            print(f" average grade {suma/liczba_kursow}")
            
    else:
        print(f"{name}: no such person in the database")


def add_course(students, name, kurs):
    if kurs[1] == 0:
        return
    
    if name in students:
        for istniejacy_kurs in students[name]:
            if istniejacy_kurs[0] == kurs[0]:
                if istniejacy_kurs[1] >= kurs[1]:
                    return  
                else:
                    students[name].remove(istniejacy_kurs)  
                    break
        students[name].append(kurs)
    else:
        students[name] = [kurs]

def summary(students):
    suma = 0
    najw = max(students, key=lambda x: len(students[x]))

  
    for i in students[najw]:
        suma += 1   

 
            
        
        


    print(f"most courses completed {suma} {najw}")
 
   


        




if __name__ == "__main__":

    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    summary(students)
  