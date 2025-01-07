# Copy here code of line function from previous exercise
def line(a, b):
    if b:
        print(a*b[0])
    else:
        print(a*"*")

    
def box_of_hashes(height):
    # You should call function line here with proper parameters
    for i in range(1, height+1):
        line(10, "#")
  

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
