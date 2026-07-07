from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner("Ishani", 90)

dog = Pet("Buddy", "Dog", 5)
cat = Pet("Luna", "Cat", 2)

dog.add_task(Task("Morning Walk", 30, 3))
dog.add_task(Task("Feed Buddy", 10, 3))
dog.add_task(Task("Brush Buddy", 15, 1))

cat.add_task(Task("Feed Luna", 10, 2))
cat.add_task(Task("Play with Luna", 20, 1))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler()
schedule = scheduler.generate_schedule(owner)

print("=" * 40)
print("🐾 PawPal+ Daily Schedule")
print("=" * 40)
print(f"Owner: {owner.name}")
print(f"Available Time: {owner.available_time} minutes\n")

for task in schedule:
    print(f"• {task.description}")
    print(f"   Duration: {task.duration} minutes")
    print(f"   Priority: {task.priority}\n")