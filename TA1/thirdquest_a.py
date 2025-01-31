r = 5

for i in range(1, r + 1):
  
    for j in range(r - i):
        print(" ", end="")

    for k in range(1, i + 1):
        print(k, end="")
 
    print()