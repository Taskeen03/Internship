class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right: return head
    dummy = ListNode(0, head)
    prev = dummy
    
    for _ in range(left - 1):
        prev = prev.next
        
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
        
    return dummy.next

head_input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

result = reverseBetween(head_input, 2, 4)

output = []
while result:
    output.append(result.val)
    result = result.next

print(output)  