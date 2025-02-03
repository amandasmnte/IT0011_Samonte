num = input("Enter a word with numbers: ")

def getsum(input_string):
    total = 0  
    for char in input_string:
        if char.isdigit():
            total += int(char)  
    return total  

result = getsum(num)  
print("\nResult: ", result) 
