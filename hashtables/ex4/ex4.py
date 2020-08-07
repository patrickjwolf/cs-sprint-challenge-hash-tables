def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # dictionary to hold all numbers in `a`
    storage = {}
    # array to return matches
    result = []
    # loop through each num in array
    for num in a:
        # if num has a corresponding number in the dictionary
        if storage.get(
                abs(num)): 
            # check if they add to 0
            if (storage.get(abs(num)) + num) == 0:
                result.append(abs(num))
        else:
            storage[abs(num)] = num
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
