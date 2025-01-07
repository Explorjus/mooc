# Copy here code of line function from previous exercise and use it in your solution
def line(a, b):
    if b:
        print(a*b[0])
    else:
        print(a*"*")

def shape(size, character, size2, character2):
    # You should call function line here with proper parameters
    for size in range(1, size + 1):
        line(size, character)
        size += 1
   
   
   
    for i in range(1, size2 +1):
        line(size - 1, character2)
    




# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")