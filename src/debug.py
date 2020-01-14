from dynamic_array import Dynamic_array
from hashtable import HashTable

def traverse(ht):
    print('Traversial')
    for i in ht.storage:
        if i != None:
            print(f'Node, {i}')
            while i != None:
                print(f"Linked Pair, Key: {i.key}, Value: {i.value}")
                i = i.next
    print(ht.capacity, '\n')

ht = HashTable(8)


ht.insert("key-0", "val-0")
ht.insert("key-1", "val-1")
ht.insert("key-2", "val-2")
ht.insert("key-3", "val-3")
ht.insert("key-4", "val-4")
ht.insert("key-5", "val-5")
ht.insert("key-6", "val-6")
ht.insert("key-7", "val-7")
ht.insert("key-8", "val-8")
ht.insert("key-9", "val-9")


ht.remove("key-9")
ht.remove("key-8")
ht.remove("key-7")
ht.remove("key-6")
ht.remove("key-5")
ht.remove("key-4")
ht.remove("key-3")
ht.remove("key-2")
ht.remove("key-1")
ht.remove("key-0")


print(ht.retrieve("key-0"))
print(ht.retrieve("key-1"))
print(ht.retrieve("key-2"))
print(ht.retrieve("key-3"))
print(ht.retrieve("key-4"))
print(ht.retrieve("key-5"))
print(ht.retrieve("key-6"))
print(ht.retrieve("key-7"))
print(ht.retrieve("key-8"))
print(ht.retrieve("key-9"))
