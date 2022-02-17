def remove_duplicates(queue):
    seen = {}

    queue.enqueue('STOP HERE')

    current = queue.dequeue()
    while current != 'STOP HERE':
        if not seen.get(current):
            seen[current] = True
            queue.enqueue(current)
        current = queue.dequeue()

    return queue
