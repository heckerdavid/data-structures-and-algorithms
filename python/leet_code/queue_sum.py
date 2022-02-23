# Given a Queue, Find the sum of all elements ... Recursively.

def queue_sum(queue):
    if queue.is_empty():
        return 0

    return queue.dequeue() + queue_sum(queue)
