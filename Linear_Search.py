def linear_search(arr,val):
    for index,num in enumerate(arr):
        if num == val:
            return [num, index+1]

    return [-1,-1]

def main():
    arr = input(("Enter a space separated list of numbers "))
    arr = [int(num) for num in arr.split()]
    value = int(input("Mention the number to search for : "))
    flag = linear_search(arr,value)
    if flag[0]==-1:
        print("This value is not present in the list")
    else:
        print(f"The value {flag[0]} is found in the list at position {flag[1]}")

if __name__=="__main__":
    main()