import time
def bubble_Sort(elements):
    size = len(elements)
    swapped = False
    swap_count = 0

    for i in range(size):
        for j in range(size-1-i):
            if elements[j]>elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1]= tmp
                swapped = True
                swap_count += 1
        if not swapped:
            break
    return elements
    # if swap_count == 0:
    #     print(f"{elements} was already sorted to begin with")


if __name__=='__main__':
    element_list = [2,5,1,87,2,9,32]
    element_list1 = [1,2,3]
    element_list2 = ['hello','what','is','your','name']

    print(bubble_Sort(element_list))
    bubble_Sort(element_list1)
    bubble_Sort(element_list2)

    # print(element_list)
    # print(element_list1)
    # print(element_list2)

    arr = [i for i in range(1000000)]

    start_time = time.time()
    sorted_arr = bubble_Sort(arr)
    end_time = time.time()
    milliseconds = (end_time - start_time) * 1000

    # print("Sorted array:", sorted_arr)
    # print("Time taken {:.6f} milliseconds".format(milliseconds))