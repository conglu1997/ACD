class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "tasks": [
                    {"name": "Task A", "duration": 2, "dependencies": []},
                    {"name": "Task B", "duration": 1, "dependencies": ["Task A"]},
                    {"name": "Task C", "duration": 3, "dependencies": ["Task A"]},
                    {"name": "Task D", "duration": 2, "dependencies": ["Task B", "Task C"]},
                    {"name": "Task E", "duration": 1, "dependencies": ["Task D"]},
                    {"name": "Task F", "duration": 2, "dependencies": ["Task E"]}
                ],
                "context": "Create an optimal schedule for the given tasks. Ensure that all dependencies are met, the total duration is minimized, and no tasks overlap improperly."
            },
            "2": {
                "tasks": [
                    {"name": "Task X", "duration": 3, "dependencies": []},
                    {"name": "Task Y", "duration": 2, "dependencies": ["Task X"]},
                    {"name": "Task Z", "duration": 4, "dependencies": ["Task Y"]},
                    {"name": "Task W", "duration": 1, "dependencies": ["Task X"]},
                    {"name": "Task V", "duration": 2, "dependencies": ["Task W"]},
                    {"name": "Task U", "duration": 1, "dependencies": ["Task Z", "Task V"]}
                ],
                "context": "Create an optimal schedule for the given tasks. Ensure that all dependencies are met, the total duration is minimized, and no tasks overlap improperly."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        tasks = t["tasks"]
        context = t["context"]
        tasks_description = "\n".join([f"- {task['name']}: duration {task['duration']} hours, dependencies: {', '.join(task['dependencies'])}" for task in tasks])
        return f"""Create an optimal schedule for the following tasks:\n
{tasks_description}\n
{context}\n
Submit your schedule as a plain text string in the following format: 'Schedule: [Your detailed schedule in hours, specifying the start and end times for each task]'.\n
Example response format:\nSchedule: Task A: 0-2, Task B: 2-3, Task C: 2-5, Task D: 5-7, Task E: 7-8, Task F: 8-10."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The schedule should meet all task dependencies.",
            "The total duration should be minimized.",
            "The schedule should be clear and logically organized.",
            "No task should start before its dependencies are completed.",
            "No tasks should overlap improperly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
