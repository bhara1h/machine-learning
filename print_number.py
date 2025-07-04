def print_numbers(m, n, k):
    for i in range(m, n + 1):
        if (i - m) % (k + 1) == 0:
            print(i)
    input_list = input("Enter the three numbers (n, m, k) separated by space: ")
    m, n, k = map(int, input_list.split())
    print(f"Updated values: m = {m}, n = {n}, k = {k}")
m, n, k = 2, 10, 3
print_numbers(m, n, k)
