from stack_and_queue.queue import Queue

class WeOnlyAcceptCatsAndDogs(Exception):
    pass

class AnimalShelter:
    def __init__(self) -> None:
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        if animal == 'dog':
            self.dogs.enqueue(animal)
        elif animal == 'cat':
            self.cats.enqueue(animal)
        else:
            raise WeOnlyAcceptCatsAndDogs

    def dequeue(self, pref):
        if pref == 'dog':
            return self.dogs.dequeue()
        elif pref == 'cat':
            return self.cats.dequeue()
        else:
            return None
