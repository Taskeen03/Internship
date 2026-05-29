class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

head_input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

result = reverseList(head_input)

output = []
while result:
    output.append(result.val)
    result = result.next

print(output) 