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

    def includes(self, value: any) -> bool:
        """Indicates whether that value exists as a Node’s value somewhere within the list."""
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
