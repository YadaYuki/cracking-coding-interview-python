from node import LinkedList

l = LinkedList(head_data=1)

data = [1,2,3,4,2,1,3,5,2,2,4]

for item in data:
    l.append_node(item)


node = l.head


print(l)

hash = {}

while node != None:
    if hash.get(node.data) == True:
        node.prev.next = node.next
    else:
        hash[node.data] = True
    node = node.next

print(hash)
print(l)