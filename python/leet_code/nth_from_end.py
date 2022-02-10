

class Solution:
    def __init__(self) -> None:
        pass
    def removeNthFromEnd(self, head, n):
        head = head
        follower = head
        leader = head

        for _ in range(n):
            if hasattr(leader, 'next'):
                leader = leader.next
            else:
                raise IndexError

        while leader.next:
            leader = leader.next
            follower = follower.next

        removed_node = follower.next
        new_next = removed_node.next
        follower.next = new_next

        return head

