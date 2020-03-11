import sys
def max_xor(arr, n): 
  
    maxXor = -sys.maxsize - 1
  
    # Calculating xor of each pair 
    for i in range(n): 
        for j in range(i + 1, n): 
            maxXor = max(maxXor, arr[i] ^ arr[j])
  
    return maxXor 

if __name__ == "__main__":
    arr = [-45, 11, 93, -77, 890, 1, 32]
    n = len(arr)
    print(max_xor(arr, n))
