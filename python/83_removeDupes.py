class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            if cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

if __name__ == "__main__":
    ob1 = Solution()
    head = [1,1,2,3,3]
    print(ob1.deleteDuplicates(head))