def print_name(name, i, n):
    if i >= n:
        print()
        return
    print(name)
    print_name(name, i + 1, n)
    return


def print_number(i, n):
    if i > n:
        print()
        return
    print(n)
    print_number(i + 1, n)


def rev_print(i, n):
    if i <= 0:
        print()
        return
    print(i)
    rev_print(i - 1, n)
    return


def backtrack_nums(i,n):
    if i<1:
        return
    backtrack_nums(i-1,n)
    print(i)

def backtrack_reverse(i,n):
    if i>n:
        return
    backtrack_reverse(i+1,n)
    print(i)

def param_nums(i,sum):
    if i < 0:
        print(sum)
        return
    return param_nums(i-1 , sum+i)

def funct_rec(n):
    if n == 0 :
        return 0
    return n + funct_rec(n-1)

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)


print_name("Striver", 0, 3)
print_number(1 , 5)
rev_print(5,5)
print("BT\n")
backtrack_nums(5,5)
print("\n")
backtrack_reverse(1,5)
param_nums(3 , 0)
print(funct_rec(3))
print(factorial(3))