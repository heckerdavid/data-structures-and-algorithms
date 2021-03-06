class Node:
    '''
    linked list node
    '''
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next




class LinkedList:
    """
    Singly linked list
    """

    def __init__(self, head=None) -> None:
        self.head = head

    def __str__(self) -> str:
        """Returns a string representing all the values in the Linked List, formatted as:
{ a } -> { b } -> { c } -> NULL"""
        string = ''
        current = self.head

        while current:
            string += '{ ' + str(current.value) + ' } -> '
            current = current.next

        string += 'NULL'

        return string

    def insert(self, value: any) -> None:
        """Inserts given value to linked list head O(1)"""
        self.head = Node(value, self.head)


    def insert_before(self, pivot, value) -> None:
        current = self.head
        previous = self.head

        if self.head.value == pivot:
            self.head = Node(value, self.head)
            return None

        while current:
            if current.value == pivot:
                previous.next = Node(value, current)
                return None
            previous = current
            current = current.next
        raise Exception(f'{pivot} not in list.')


    def insert_after(self, pivot, value):
        current = self.head
        previous = self.head

        while current:
            if current.value == pivot:
                current.next = Node(value, current.next)
                return None
            previous = current
            current = current.next

    def kth_from_the_end(self, k):
        finder = self.head
        follower = self.head
        length = 0

        if finder is None or k < 0:
            return

        while finder.next:
            length += 1
            finder = finder.next

        if k > length:
            return f'{k} is larger than the length of this list'

        for _ in range(length - k):
            follower = follower.next

        return follower.value


    def append(self, value) -> None:
        current = self.head
        if current is None:
                self.head = Node(value)
        while current:
            if current.next is None:
                current.next = Node(value)
                break
            current = current.next


    def includes(self, value: any) -> bool:
        """Indicates whether that value exists as a Node???s value somewhere within the list."""
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next
        return False


    def delete(self, value) -> str:
        """Removes first instance of given value from list. O(n)"""
        current = self.head
        previous = self.head

        while current:
            if current.value == value:
                previous.next = current.next
                return f'{current.value} deleted from list.'
            previous = current
            current = current.next
        return f'Cannot delete {value}; {value} not found in list.'


    def get_length(self, node, working_length=0) -> int:
        if node is None:
            return working_length
        return self.get_length(node.next, working_length + 1)

