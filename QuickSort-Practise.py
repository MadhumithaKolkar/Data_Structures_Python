def swap(start,end,elements):
    if start!= end:
        tmp = elements[start]
        elements[start] = elements[end]
        elements[end] = tmp

def quick_sort(start,end,elements):
    if start<end :
        pi = partition(start,end,elements)
        quick_sort(start,pi-1,elements)
        quick_sort(pi+1, end, elements)

def partition(start, end, elements):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start<len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if(start<end):
            swap(start,end,elements)

    swap(pivot_index,end,elements)
    return end

if __name__ == '__main__':
    # elements = [11, 9, 29, 7, 2, 15, 28]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(0, len(elements) - 1, elements)
    print(elements)
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    for entry in tests:
        quick_sort(0,len(entry)-1, entry)
        print(entry)