#INSERTION SORT
n = [int(x) for x in input("Give integers as input").split()]
print("Printing after each step")
for i in range(1,len(n)):
    key = n[i]
    j=i-1
    while j>=0 and n[j] > key:
        n[j+1]=n[j]
        j-=1
    n[j+1]=key    
    print("Step" + str(i-1) +":" , end=' ')
    print(n)
print("sorted output")
print(n)
#N = SIZE OF INPUT
#TIME COMPLEXITY O(N^2)
#SPACE COMPLEXITY O(1)
#intro to algorithms cormen
        
    

