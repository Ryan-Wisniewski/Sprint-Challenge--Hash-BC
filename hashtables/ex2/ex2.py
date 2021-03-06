#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    while True:
        for i in range(len(tickets)):
            hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
            # print('@@@', tickets[i].source, tickets[i].destination)
        for i in range(len(tickets)):
            retrieve = hash_table_retrieve(hashtable, tickets[i].source)
            print('@',retrieve)
            if retrieve == None:
                print('None hopefully removed')
                pass
                
            elif hashtable.storage[i] == None:
                print('hashtable storage NONE')
                hash_table_remove(hashtable, tickets[i].source)
                pass
                
            elif retrieve == hashtable.storage[i].value:
                route[i] = tickets[i].destination
                print(retrieve, hashtable.storage[i].value)
                hash_table_remove(hashtable, tickets[i].source)
            else: print('f')
        
    return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# # expected = ["PDX", "DCA", "NONE"]
# result = reconstruct_trip(tickets, 3)
# print(result)



ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# expected = ["LAX", "SFO", "BHM", "FLG", "XNA", "SAP",
#             "SLC", "PIT", "ORD", "NONE"]
result = reconstruct_trip(tickets, 10)

print(result)