# Write your solution here
def filter_solutions():
    with open("solutions.csv", "r") as my_file:
        dobre = []
        niedobre = []
        
        for line in my_file:
            fields = line.strip().split(';')
           

            print(fields)     

            if fields[1] == fields[2]:
                dobre.append(fields)
                
                with open("correct.csv", "w") as poperawne:
                    poperawne.write(line)
            else:
                niedobre.append(fields)



                with open("incorrect.csv", 'w') as niepoprawne:
                    niepoprawne.write(line)

        
