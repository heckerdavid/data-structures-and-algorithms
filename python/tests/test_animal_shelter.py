from stack_and_queue.underflow import UnderFlowError
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter
import pytest

def test_import():
    assert AnimalShelter()

def test_enqueue_dogs():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('dog')

    actual = shelter.dequeue('dog')
    expected = 'dog'
    assert actual == expected


def test_enqueue_dogs_and_cats():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')

    actual = shelter.dequeue('dog')
    expected = 'dog'
    assert actual == expected

def test_enqueue_dogs_and_cats2():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')

    actual = shelter.dequeue('cat')
    expected = 'cat'
    assert actual == expected

def test_dequeue_dogs_and_cats_():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')

    shelter.dequeue('cat')
    shelter.dequeue('cat')
    shelter.dequeue('cat')
    with pytest.raises(UnderFlowError):
        shelter.dequeue('cat')

def test_dequeue_dogs_and_cats2():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')

    shelter.dequeue('dog')
    shelter.dequeue('dog')

    with pytest.raises(UnderFlowError):
        shelter.dequeue('dog')
