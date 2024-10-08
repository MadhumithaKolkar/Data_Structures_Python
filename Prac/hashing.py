def find_count(arr):
    count = {}
    for i in range(len(arr)):
        count[arr[i]] = 1 + count.get(arr[i], 0)
    return count


# counts = find_count([1, 2, 45, 23, 6, 12, 1, 1, 2, 2, 23, 23])

# n = int(input())
# test_vals = []
# input_str = input()
# input_list = list(map(int,input_str.split()))
# while True:
#     line = input().strip()
#     if line == "":
#         break
#     test_vals.append(int(line))
#
# vals = find_count(input_list)
# for num in test_vals:
#     print(f"Number : {num}, count : {vals.get(num,0)}")

# str = input()
# str_c = {}
# for ch in str:
#     str_c[ch] = 1+str_c.get(ch,0)
#
# for ch,val in str_c.items():
#     print(f"{ch} : {val}")
#
arr = [10,5,10,15,10,5,3,3,3,3]
count = {}
for num in arr:
    count[num] = 1+count.get(num,0)

highest = float("-inf")
lowest = float("inf")
freq_highest = 0
freq_lowest = float("inf")

for num,val in count.items():
    if val>freq_highest:
        highest = num
        freq_highest = val
    if val<freq_lowest:
        lowest = num
        freq_lowest = val

print(f"Highest : {highest}, Lowest : {lowest}")
