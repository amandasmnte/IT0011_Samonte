
filename = 'numbers.txt'

try:
    with open(filename, 'r') as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
      
        numbers = line.strip().split(',')
        
       
        valid_numbers = []
        
        for num in numbers:
            try:
             
                valid_numbers.append(int(num.strip()))  
            except ValueError:
                print(f"Warning: '{num}' is not a valid number and will be ignored.")

       
        total_sum = sum(valid_numbers)
        
       
        if str(total_sum) == str(total_sum)[::-1]:
            palindrome_status = "Palindrome"
        else:
            palindrome_status = "Not a palindrome"
        
     
        print(f"Line {index + 1}: {','.join(map(str, valid_numbers))} (sum {total_sum}) - {palindrome_status}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")