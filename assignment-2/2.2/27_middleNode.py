class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head_input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

result = middleNode(head_input)

output = []
while result:
    output.append(result.val)
    result = result.next

print(output) 