 #The user input 
user_input = input ("Enter a word or sentence: ")

    
#  Use for loop and operators
def analyze (user_input) :
    type_v = 0
    type_con = 0
    type_spa = 0
    type_char = 0
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    for char in user_input:
        if char in vowels:
            type_v +=1
            type_char+=1
        elif char in consonants:
            type_con +=1
            type_char+=1
        elif char == " ":
            type_spa +=1
        else:
            pass
            
    print("\nOutput \n")
    print("Number of vowels:" , type_v)
    print("Numbeer of consonants: ", type_con)
    print("Number of spaces: ", type_spa)
    print("Number of characters: ", type_char)

analyze (user_input)
