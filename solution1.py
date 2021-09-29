def staircase(n):
    for i in range(1,n+1):
        for j in range(n-1):
            print(" ", end="")
            
        print("#"*i)
        n -= 1
        
staircase(5)
