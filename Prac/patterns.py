def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


def pattern2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()


def pattern3(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()


def pattern4(n):
    for i in range(n):
        for j in range(i + 1):
            print(i + 1, end=" ")
        print()


def pattern5(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()


def pattern6(n):
    for i in range(n):
        for j in range(n - i):
            print(j + 1, end=" ")
        print()


def pattern7(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()


def pattern8(n):
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1), end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()


def pattern9(n):
    for i in range(2 * n - 1):
        if i < n:
            for j in range(i + 1):
                print("*", end="")
        else:
            for j in range(2 * n - i - 1):
                print("*", end="")
        print()


def pattern10(n):
    for i in range(n):
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i + 1):
            print(start, end="")
            start = 1 - start
        print()


def pattern11(n):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end="")
        for j in range(2 * n - 2 * i - 2):
            print(" ", end="")
        for j in range(i + 1, 0, -1):
            print(j, end="")
        print()

def pattern12(n):
    start = 1
    for i in range(n):
        for j in range(i+1):
            print(start,end=" ")
            start+=1
        print()

def pattern13(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord("A")+j),end="")
        print()

def pattern14(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(ord("A")+j),end="")
        print()

def pattern15(n):
    start = ord("A")
    for i in range(n):
        for j in range(i+1):
            print(chr(start),end="")
        print()
        start += 1

def pattern16(n):
    start = ord("A")
    # for i in range(n):
    #     for j in range(n-i-1):
    #         print(" ",end="")
    #     for j in range(i+1):
    #         print(chr(ord("A")+j) , end="")
    #         last = ord("A")+j
    #     for j in range(i):
    #         print(chr(last-j-1), end = "")
    #     print()
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        ch = ord("A")-1
        for j in range(2*i+1):
            if j>i:
                ch -= 1
                print(chr(ch),end="")
            else:
                ch += 1
                print(chr(ch) , end = "")
        print()

def pattern17(n):
    for i in range(n):
        ch = ord("A")+n-i-1
        for j in range(i+1):
            print(chr(ch) , end = "")
            ch += 1
        print()

def pattern18(n):
    # for i in range(2*n):
    #     if i<n:
    #         for j in range(n-i):
    #             print("*" , end = "")
    #         for j in range(2*i):
    #             print(" " , end = "")
    #         for j in range(n-i):
    #             print("*" , end = "")
    #     else:
    #         for j in range(i%n+1):
    #             print("*" , end = "")
    #         num = 2 * n - 2*(i%n+1)
    #         for j in range(num):
    #             print(" " , end = "")
    #             # num -= 2
    #         for j in range(i%n+1):
    #             print("*" , end = "")
    #     print()
    for i in range(n):
            for j in range(n-i):
                print("*" , end = "")
            for j in range(2*i):
                print(" " , end = "")
            for j in range(n-i):
                print("*" , end = "")
            print()
    for i in range(n):
            for j in range(i+1):
                print("*" , end = "")
            num = 2 * n - 2*i -2
            for j in range(num):
                print(" " , end = "")
                # num -= 2
            for j in range(i+1):
                print("*" , end = "")
            print()

def pattern19(n):
    # for i in range(n):
    #     for j in range(i+1):
    #         print("*" , end = "" )
    #     for j in range(2*n-2*i-2):
    #         print(" " , end = "" )
    #     for j in range(i+1):
    #         print("*" , end = "" )
    #     print()
    # for i in range(1,n,1):
    #     for j in range(n-i):
    #         print("*" , end = "" )
    #     for j in range(2*i):
    #         print(" " , end = "" )
    #     for j in range(n-i):
    #         print("*" , end = "" )
    #     print()
    spaces = 2*n
    for i in range(2*n):
        stars = i+1
        if(i>=n) : stars =2*n-i-1
        if i>=n:
            spaces += 2
        else:
            spaces -= 2

        for j in range(stars):
            print("*" , end = "" )
        for j in range(spaces):
            print(" " , end = "" )
        for j in range(stars):
            print("*" , end = "" )
        print()

def pattern20(n):
    # for i in range(n):
    #     if(i+1==n or i==0):
    #         stars = n
    #         spaces = 0
    #     else:
    #         stars = 1
    #         spaces = 2*n-2
    #     for j in range(stars):
    #         print("*" , end = "" )
    #     for j in range(spaces):
    #         print(" " , end = "" )
    #     for j in range(stars):
    #         print("*" , end = "" )
    #     print()
    for i in range(n):
        for j in range(n):
            if(i==0 or i==n-1 or j==0 or j==n-1 ):
                print("*" , end = "" )
            else:
                print(" ", end = "" )
        print()

def pattern21(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            bottom = j
            left = (2*n)-2-j
            right = ( 2 * n ) - 2 - j
            print( n - min ( min ( top , bottom ) , min ( left , right )) , end = "")
        print()
pattern1(4)
pattern2(4)
pattern3(4)
pattern4(4)
pattern5(4)
pattern6(4)
pattern7(4)
pattern8(4)
pattern9(4)
pattern10(4)
pattern11(4)
pattern12(4)
pattern13(4)
pattern14(4)
pattern15(4)
pattern16(4)
pattern17(5)
pattern18(4)
pattern19(4)
pattern20(4)
pattern21(4)