def removeNthFromEnd(head, n):
    fast, slow = head, head
    for _ in range(n): fast = fast.next
    if not fast: return head.next
    while fast.next: fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return head

    

if __name__ == "__main__":
    head = [1,2,3,4,5]
    n = 2
    print(removeNthFromEnd(head,n))