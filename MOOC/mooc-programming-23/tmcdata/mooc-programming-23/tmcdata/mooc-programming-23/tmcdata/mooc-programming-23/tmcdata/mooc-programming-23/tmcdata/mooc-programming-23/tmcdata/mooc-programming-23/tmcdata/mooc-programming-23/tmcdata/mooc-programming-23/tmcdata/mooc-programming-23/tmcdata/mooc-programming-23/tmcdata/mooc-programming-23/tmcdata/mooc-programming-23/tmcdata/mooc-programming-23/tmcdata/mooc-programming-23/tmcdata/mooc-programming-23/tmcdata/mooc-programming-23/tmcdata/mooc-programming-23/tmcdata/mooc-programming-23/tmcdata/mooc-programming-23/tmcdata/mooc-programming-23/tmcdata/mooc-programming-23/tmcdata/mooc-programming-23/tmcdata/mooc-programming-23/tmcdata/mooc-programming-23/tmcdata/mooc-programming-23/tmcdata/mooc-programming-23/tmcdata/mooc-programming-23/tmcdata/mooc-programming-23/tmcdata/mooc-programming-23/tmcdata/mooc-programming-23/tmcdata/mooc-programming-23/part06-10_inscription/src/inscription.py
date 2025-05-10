# Write your solution here
kto = input("Whom should I sign this to: ")
zapis = input("Where shall I save it: ")

with open(zapis, "w") as my_file:
    my_file.write(f"Hi {kto}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")