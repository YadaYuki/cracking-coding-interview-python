# 2.5
from linked_list import LinkedList,Node

def sum_linked_list(a:LinkedList,b:LinkedList) -> LinkedList:
    na,nb = a.head,b.head
    
    # calc head data
    head_data = na.data + nb.data
    l_sum:LinkedList = None
    flag = 0

    if head_data >= 10:
        l_sum = LinkedList(head_data = head_data-10)
        flag = 1
    else :
        l_sum = LinkedList(head_data=head_data)
    
    na,nb = na.next,nb.next

    while (na is not None) and  (nb is not None):
        # calculate sum
        n_data = (na.data + nb.data + flag) % 10
        flag = int((na.data + nb.data + flag) / 10)
        l_sum.append_node(data=n_data)
        # next digit
        na,nb = na.next,nb.next
    
    while na is not None:
        l_sum.append_node(na.data+flag)
        na = na.next
        flag = 0 
    while nb is not None:
        l_sum.append_node(nb.data+flag)
        nb = nb.next
        flag = 0 

    if flag == 1:
        l_sum.append_node(data=1)

    return l_sum

if __name__ == "__main__":

    a,b = [7,1,6],[5,9,5,2,1]
    la,lb = LinkedList(head_data=a[0]),LinkedList(head_data=b[0])

    for item in a[1:]:
        la.append_node(item)
    for item in b[1:]:
        lb.append_node(item)
    
    ans = sum_linked_list(la,lb)
    
    print(ans) # 2 -> 1 -> 9 ->

