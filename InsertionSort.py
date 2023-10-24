def insertionSort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j = i-1
        while j>=0 and anchor<elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

if __name__ == '__main__':
    array = [5,2,1,0,7,9,3]
    insertionSort(array)
    print(array)