from linked_list import ListNode

def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original list:")
print_list(head)

reversed_head = reverse_list(head)

print("Reversed list:")
print_list(reversed_head)