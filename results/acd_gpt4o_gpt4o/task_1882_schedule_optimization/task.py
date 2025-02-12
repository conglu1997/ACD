class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "tasks": [
                    {"name": "Task A", "duration": 2, "priority": 1},
                    {"name": "Task B", "duration": 1, "priority": 2},
                    {"name": "Task C", "duration": 3, "priority": 1},
                    {"name": "Task D", "duration": 2, "priority": 3},
                    {"name": "Task E", "duration": 1, "priority": 2}
                ],
                "constraints": {
                    "max_hours_per_day": 4,
                    "days": 3,
                    "mandatory_tasks": ["Task A", "Task C"],
                    "max_tasks_per_day": 3
                }
            },
            "2": {
                "tasks": [
                    {"name": "Task F", "duration": 4, "priority": 2},
                    {"name": "Task G", "duration": 1, "priority": 3},
                    {"name": "Task H", "duration": 2, "priority": 1},
                    {"name": "Task I", "duration": 1, "priority": 2},
                    {"name": "Task J", "duration": 2, "priority": 1}
                ],
                "constraints": {
                    "max_hours_per_day": 5,
                    "days": 2,
                    "mandatory_tasks": ["Task H", "Task J"],
                    "max_tasks_per_day": 3
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        tasks = '\n'.join([f'{task["name"]} (Duration: {task["duration"]} hours, Priority: {task["priority"]})' for task in t["tasks"]])
        constraints = t["constraints"]
        instructions = f"""Your task is to create and optimize a schedule for the following tasks based on the given constraints.

Tasks:
{tasks}

Constraints:
- Maximum hours per day: {constraints["max_hours_per_day"]}
- Number of days: {constraints["days"]}
- Mandatory tasks: {', '.join(constraints["mandatory_tasks"])}, which must be completed.
- Maximum tasks per day: {constraints["max_tasks_per_day"]}

Guidelines:
1. Prioritize tasks based on their priority levels (1 is the highest priority).
2. Ensure that the total hours for each day do not exceed the maximum hours per day.
3. Ensure that the number of tasks per day does not exceed the maximum tasks per day.
4. Ensure that mandatory tasks are completed.
5. Try to complete all tasks within the given number of days.
6. Provide the schedule in a clear and organized format.

Provide your response in the following format:

Schedule:
Day 1: [Task names with durations]
Day 2: [Task names with durations]
...

Example Schedule:
Day 1: Task A (2 hours), Task B (1 hour)
Day 2: Task C (3 hours)
Day 3: Task D (2 hours), Task E (1 hour)
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The schedule should prioritize tasks based on their priority levels.",
            "The schedule should not exceed the maximum hours per day.",
            "The schedule should aim to complete all tasks within the given number of days.",
            "The schedule should ensure that mandatory tasks are completed.",
            "The schedule should ensure that the number of tasks per day does not exceed the maximum tasks per day.",
            "The schedule should be clear and organized."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
