def dummy(num,count):
    print(f"In iter : {count}")
    if count == 10:
        return f"   The value of the number now is {num}"
    return dummy(num*5,count+1)

print(dummy(5,1))
print(5**10)