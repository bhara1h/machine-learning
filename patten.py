def print_patten(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end='')
        print()
n=int(input("enter the numbers of rows:"))
print_patten(n)
