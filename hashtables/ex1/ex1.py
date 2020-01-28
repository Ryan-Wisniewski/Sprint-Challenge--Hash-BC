#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i in range(len(weights)):
        print(weights[i], i)
        key = i
        value = weights[i]
    for j in range(len(weights)):
        hash_table_insert(ht, key, value)
        print(ht)
        retrieve = hash_table_retrieve(ht, i)
        print('yeet',retrieve)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))