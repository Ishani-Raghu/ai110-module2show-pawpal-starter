# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial UML design included four main classes: **Owner**, **Pet**, **Task**, and **Scheduler**. The `Owner` class stores the owner's information and manages a collection of pets. The `Pet` class stores information about each pet and its associated care tasks. The `Task` class represents individual pet care activities, including a description, duration, priority, and completion status. The `Scheduler` class is responsible for organizing tasks, sorting them by priority, filtering tasks based on the owner's available time, and generating a daily schedule.

### b. Design changes

During implementation, I simplified the scheduling logic by focusing on task priority and available time instead of implementing more advanced features such as recurring tasks or conflict detection. This allowed me to complete a working scheduling system while keeping the code organized and easy to understand.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

My scheduler considers two primary constraints: the owner's available time and the priority assigned to each task. Tasks with higher priority are scheduled first, and only tasks that fit within the owner's available time are included in the final schedule. I chose these constraints because they have the greatest impact on creating a practical daily plan for pet care.

### b. Tradeoffs

One tradeoff my scheduler makes is that it only sorts tasks by priority and does not consider exact times or overlapping appointments. This simplifies the scheduling algorithm while still ensuring that the most important pet care tasks are completed first. For this project, that tradeoff is reasonable because the focus is on demonstrating object-oriented programming and scheduling logic rather than building a full calendar application.

---

## 3. AI Collaboration

### a. How you used AI

I used AI throughout the project to brainstorm the initial class design, generate the UML diagram, debug Python errors, improve my scheduler logic, and create automated tests. The most helpful prompts were questions about fixing errors, organizing classes, and improving the readability of my code.

### b. Judgment and verification

At one point, AI suggested implementing more advanced scheduling features than my project currently required. Instead of adding unnecessary complexity, I kept my simpler priority-based scheduler because it satisfied the project requirements and was easier to test and maintain. I verified AI suggestions by running my program, checking the output, and confirming that all pytest tests passed successfully.

---

## 4. Testing and Verification

### a. What you tested

I tested adding pets to an owner, adding tasks to pets, and marking tasks as completed. These tests ensured that the core object-oriented functionality worked correctly before generating schedules.

### b. Confidence

I am confident that my scheduler performs its core functions correctly because the application runs successfully and all automated tests pass. If I had more time, I would test additional edge cases such as owners with no pets, pets with no tasks, tasks with equal priorities, and situations where the available time is zero.

---

## 5. Reflection

### a. What went well

The part of this project I am most satisfied with is designing the object-oriented structure. Separating the project into Owner, Pet, Task, and Scheduler classes made the code easier to organize, understand, and maintain.

### b. What you would improve

If I had another iteration, I would add recurring tasks, conflict detection, and time-based scheduling. I would also expand the Streamlit interface to allow users to edit and remove tasks directly from the application.

### c. Key takeaway

One important lesson I learned is that designing the system before writing code makes implementation much easier. I also learned that AI is a valuable tool for brainstorming, debugging, and improving code, but it is still important to evaluate its suggestions, verify the results, and choose the solutions that best fit the project's requirements.
