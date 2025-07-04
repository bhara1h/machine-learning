
def is_perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(num, "is a Perfect number")
else:
    print(num, "is not a Perfect number")
