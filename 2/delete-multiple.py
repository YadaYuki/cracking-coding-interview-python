from linked_list import LinkedList

l = LinkedList(head_data=1)

data = [1,2,3,4,2,1,3,5,2,2,4]

for item in data:
    l.append_node(item)

hash = {}
print("Before:{}".format(l))
node = l.head
previous = None
while node != None:
    if hash.get(node.data) == True:
        previous.next = node.next
    else:
        hash[node.data] = True
        previous = node
    node = node.next
print("After:{}".format(l))