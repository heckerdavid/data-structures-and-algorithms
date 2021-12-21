from stack_and_queue.queue import Queue

def breadth_first(tree) -> list:
    if tree.root is None:
        return []

    value_list = []
    queue = Queue()

    queue.enqueue(tree.root)

    while queue.peek():
        current = queue.dequeue()
        queue.enqueue(current.left)
        queue.enqueue(current.right)
        value_list.append(current.value)

    return value_list
