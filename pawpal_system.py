from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    duration: int
    priority: int
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


@dataclass
class Owner:
    name: str
    available_time: int
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return every task from every pet."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.tasks)
        return all_tasks


class Scheduler:
    """Creates a daily schedule."""

    def sort_tasks(self, tasks):
        """Sort by priority (highest first)."""
        return sorted(tasks, key=lambda task: task.priority, reverse=True)

    def filter_tasks(self, tasks, available_time):
        """Only include tasks that fit in available time."""
        selected = []
        total = 0

        for task in tasks:
            if total + task.duration <= available_time:
                selected.append(task)
                total += task.duration

        return selected

    def generate_schedule(self, owner):
        """Generate today's schedule."""
        tasks = owner.get_all_tasks()
        tasks = self.sort_tasks(tasks)
        return self.filter_tasks(tasks, owner.available_time)