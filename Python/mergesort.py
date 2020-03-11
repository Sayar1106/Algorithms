import random
import time
start_time = time.time()

def mergeSort(inputseq):
    if len(inputseq) > 1:
        mid = len(inputseq)//2
        leftside = inputseq[:mid]
        rightside = inputseq[mid:]
        mergeSort(leftside)
        mergeSort(rightside)
        i=j=k=0
        while i < len(leftside) and j < len(rightside):
            if leftside[i] < rightside[j]:
                inputseq[k] = leftside[i]
                i += 1 
            else:
                inputseq[k] = rightside[j]
                j += 1 
            k += 1
        while i < len(leftside):
            inputseq[k] = leftside[i]
            i += 1
            k += 1
        while j < len(rightside):
            inputseq[k] = rightside[j]
            j += 1
            k += 1
    print("Merged {}".format(inputseq))
   


if __name__ == "__main__":
    myList = [random.randint(0,1000) for i in range(10)]
    print("List before sorting: {}".format(myList))
    mergeSort(myList)
    print("List after sorting: {}".format(myList))
    print("--- %s seconds ---" % (time.time() - start_time))

