def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight = {}
    duplicate_check = False
    duplicates = {}  # account for duplicate values
    # iterate through weights and store them in the dictionary
    for i in range(0, length):
        current = weights[i]
        weight[current] = i  # set the value to the index
        # subtract current value from the limit to find which package combines to equal weight limit
        target = limit - current
        if target in weight:
            if current > target:
                return (i, weight[target]) 
            elif current < target:
                return (i, weight[target])
            elif target == current:  # if it finds a duplicate
                if duplicate_check is False:  # that isnt already classified as a duplicate
                    duplicate_check = True
                    duplicates[current] = i  # set the value to the index
                elif duplicate_check is True:
                    return (i, duplicates[current])
    return None

    return None
