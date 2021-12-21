from stack_and_queue.queue import Queue

def breadth_first(tree) -> list:
    if tree.root is None:
        return []
