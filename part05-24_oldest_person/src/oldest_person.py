# Write your solution here
def oldest_person(people: list):
 
    
    oldest = min(people, key=lambda x: x[1])  #key=lambda x: x[1] oznacza, że funkcja min() 
    #                                porównuje pierwsze elementy krotek, aby znaleźć najmniejszy.
    #najm = people[1]
    #for i in people:
    #   if i[1] < najm[1]:
    #       najm = i
    #return najm[1]
    return oldest[0]
 



if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
  
    print(oldest_person(people))