def productbutitself(array):
    prod = 1
    res = []
    for item in array:
        prod *= item

    for item in array:
        res.append(prod/item)
    
    return res

if __name__ == "__main__":

    array = [1, 3, 5, 7]

    res = productbutitself(array)

    print(res)


