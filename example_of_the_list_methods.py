from contiguous_list_class import *

list = List(20)

for i in range(10, -1, -1):
    list.insert(i, 0)

print("LIST:", list)

print("LIST LENGTH METHOD:", list.length())

list.insert("IN THE MIDDLE", 6)
print("INSERTION IS POSSIBLE IN ANY VALID INDEX:", list)

list.remove(6)
print("LIST AFTER REMOVING THE ITEM IN INDEX 6:", list)

print("GETTING AN INDEX THROUGH A VALUE:", list.get_index(0))

print("GETTING A VALUE THROUGH AN INDEX:", list.get_item(10))
