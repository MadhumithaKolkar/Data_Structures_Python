import math


def reverse(n):
    reversed_number = 0
    while n>0:
        last_digit = n%10
        n = n//10
        reversed_number = reversed_number*10 + last_digit
    return reversed_number

def count_digits(n):
    # count = 0
    # while n>0:
    #     n = n//10
    #     count += 1
    # return count
    # if n == 0 : return 1

    return int(math.log10(n))+1

def check_palindrome(n):
    num = n
    rev = 0
    while num>0:
        last_digit = num%10
        num = num//10
        rev = rev*10 + last_digit
    if rev == n : print("Palindrome")
    else: print("Not a palindrome")

def check_armstrong(n):
    num = n
    count = int(math.log10(num))+1
    # or len(str(num))
    sum = 0
    while num>0:
        last_digit = num%10
        num = num//10
        sum += last_digit**count
    if sum==n : print("Armstrong")
    else : print("Not Armstrong ..")

def print_divisors(n):
    # for i in range(1,n+1,1):
    #     if n%i==0:
    #         print(i,end= ",")
    i = 1  # Start from 1 to avoid division by zero
    list = []
    while i <= math.sqrt(n):
        if n % i == 0:
            list.append(i)  # Print the divisor i
            if (n // i) != i:  # Check if it's not a duplicate divisor
                list.append(n//i)  # Print the corresponding divisor n // i
        i += 1
    return list

def prime(n):
    counter = 0
    for i in range(1,int(math.sqrt(n))+1,1):
        if n%i==0:
            counter += 1
            if (n//i)!=i:
                counter += 1
    if counter == 2 : print("Prime")
    else : print("Not Prime ..")

def gcd(n1,n2):
    # gcd = 1
    # for i in range(min(n1,n2),0,-1):
    #     if (n1%i==0 and n2%i==0):
    #         gcd = i
    #         return gcd
    while n1>0 and n2>0:
        if n1>n2 : n1 = n1-n2
        else : n2 = n2-n1
    if n1==0 : return n2
    return n1

print(reverse(77890))
print(count_digits(10000))
check_palindrome(1214)
check_armstrong(1634)
print(print_divisors(36))
prime(33)
print(gcd(20,41))