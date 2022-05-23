def pyramid(numOfLines):
  line = numOfLines-1
  odd = 1
 
  for i in range(0,numOfLines):
    for j in range(0,line):
      print(end=" ")
    for k in range(0, odd):   
      print("*", end="")

    line -= 1
    odd += 2
    
    print()

n = int(input("Enter the number of lines for the Pyramid: \n"))
print()
pyramid(n)