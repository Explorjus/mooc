# Copy here code of line function from previous exercise
def line(a, b):
    if b:
        print(a*b[0])
    else:
        print(a*"*")


def triangle(size):
    # You should call function line here with proper parameters
    for i in range(1, size+ 1):    
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
