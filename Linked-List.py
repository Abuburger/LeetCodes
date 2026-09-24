class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def linked_to_list(h):
    result = []
    curr = h

    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    return result

def reversedList(h):
    curr = head
    previous = None 
    while curr is not None:
        temp = curr.next
        curr.next = previous 
        previous = curr
        curr = temp 
    return linked_to_list(previous)



head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
print(reversedList(head))
