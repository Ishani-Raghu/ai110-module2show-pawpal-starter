from pawpal_system import Owner, Pet, Task


def test_add_pet():
    owner = Owner("Ishani", 60)
    pet = Pet("Buddy", "Dog", 5)

    owner.add_pet(pet)

    assert len(owner.pets) == 1


def test_add_task():
    pet = Pet("Buddy", "Dog", 5)

    pet.add_task(Task("Walk", 30, 3))

    assert len(pet.tasks) == 1


def test_mark_complete():
    task = Task("Feed", 10, 3)

    task.mark_complete()

    assert task.completed

  
