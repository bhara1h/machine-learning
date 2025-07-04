def is_palindrome(x:int)-> bool:
    return str(x)==str(x)[::-1]
x=int(input("enter the integer:"))
print(is_palindrome(x))
