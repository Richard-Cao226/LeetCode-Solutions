class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        sumNode = ListNode()
        result = sumNode
        carry = 0
        while node1 is not None or node2 is not None:
            if node1 is not None and node2 is not None:
                sum = node1.val + node2.val + sumNode.val
            elif node1 is not None:
                sum = node1.val + sumNode.val
            elif node2 is not None:
                sum = node2.val + sumNode.val
            if (sum > 9):
                sumNode.val = sum % 10
                carry = sum // 10
            else:
                sumNode.val = sum
                carry = 0
            
            if node1 is not None and node1.next is not None or node2 is not None and node2.next is not None:
                sumNode.next = ListNode(carry)
                sumNode = sumNode.next
            elif node1 is not None and node1.next is None and node2 is not None and node2.next is None and carry != 0:
                sumNode.next = ListNode(carry)
                break
            if node1 is not None:
                node1 = node1.next
            if node2 is not None:
                node2 = node2.next    
        if carry != 0:
            sumNode.next = ListNode(carry)
        return result