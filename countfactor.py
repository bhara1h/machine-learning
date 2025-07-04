def count_factor(n):
    count=0
    for i in range(1,n+1):
        if n % i ==0:
            count +=1
            return count
n=int(input("enter the numbers:"))
print("the factor for",n,"is:",count_factor(n))
