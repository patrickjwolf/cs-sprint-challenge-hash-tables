#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    flights = {}
    route = [None] * length  # create route list with sufficient size
    for i in range(0, length):
        current = tickets[i]
        flights[current.source] = current.destination
    # set first flight in arr  with source "NONE"
    route[0] = flights["NONE"]

    route[1] = flights[route[0]]  # ReadMe hint

    if length > 2:
        for i in range(2, length):
            # the `i`th location in the route can be found by checking the hash
            # table for the `i-1`th location
            route[i] = flights[route[i - 1]]
    return route

    return route
