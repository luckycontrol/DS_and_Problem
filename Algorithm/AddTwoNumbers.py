from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def devide(num):
    if num >= 10:
        return [num // 10, num % 10]
    else:
        return [0, num]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        carry = 0
        root = n = ListNode(0)

        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = devide(v1 + v2 + carry)
            n.next = ListNode(val)
            n = n.next

        return root.next


if __name__ == "__main__":
    a = b = ListNode(5)
    b.val = 3

    b = b.next
    print(id(a))
    print(id(b))
