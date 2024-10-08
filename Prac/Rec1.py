def rev_1(l, r, a):
    a_copy = a[:]
    if l >= r:
        return a_copy
    a_copy[l], a_copy[r] = a_copy[r], a_copy[l]
    return rev_1(l + 1, r - 1, a_copy)


def rev_2(i, a):
    a_copy = a[:]
    if i >= len(a_copy) // 2:
        return a_copy
    a_copy[i], a_copy[n - i - 1] = a_copy[n - i - 1], a_copy[i]
    return rev_2(i+1,a_copy)

def check_pal(i,a,n):
    if i>(n//2):
        return True
    if a[i] != a[n-i-1]:
        return False
    return check_pal(i+1,a,n)

def fib(n):
    if n<=1:
        return n
    last = fib(n-1)
    s_last = fib(n-2)
    return last+s_last


a = [1, 2, 3, 4, 5]
n = len(a)
ans1 = rev_1(0, n - 1, a)
print(ans1)

ans2 = rev_2(0 , a)
print(ans2)
a = "MADAM"
print(check_pal(0,a,len(a)))
print(fib(9))
