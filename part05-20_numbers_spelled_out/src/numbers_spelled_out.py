# Write your solution here
def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    nowa = {}

    for i in range(10):
        nowa[i] = ones[i]
    
    for i in range(10,20):
        nowa[i] = teens[i - 10]

    for i in range(20, 100):
        tenn_miej = i // 10    #dzielenie calkowite zwraca 4
        ones_miej = i % 10     #dzielnie zwraca reszte z dzielnia

        if ones_miej == 0:
            nowa[i] = tens[tenn_miej]  #jesli miejsce jednosci to 0 dodawna jest tylko liczba dziesiatek
        else:
            nowa[i] = tens[tenn_miej] + '-' + ones[ones_miej]

    return nowa
        
if __name__ == "__main__":
    
    numbers = dict_of_numbers()
    print(numbers[2])  
    print(numbers[11])  
    print(numbers[45])  
    print(numbers[99])  
    print(numbers[0])