from collections import Counter

def intersection(arrays):
    """
    YOUR CODE HERE
    """

    dict = {}
    result = []

    for arr in arrays:
        for num in arr:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
            if dict[num] == len(arrays):
                result.append(num)
    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
