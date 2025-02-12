class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "employees": ["Alice", "Bob", "Charlie", "Diana"],
                "shifts": ["morning", "afternoon", "night"],
                "constraints": [
                    "Alice cannot work night shifts.",
                    "Bob must work at least 2 morning shifts.",
                    "Charlie and Diana cannot work the same shift.",
                    "Each employee must work exactly 5 shifts in a week.",
                    "No employee can work more than 2 consecutive shifts."
                ]
            },
            "2": {
                "tasks": ["Task A", "Task B", "Task C", "Task D"],
                "time_slots": ["8-10 AM", "10-12 PM", "1-3 PM", "3-5 PM"],
                "constraints": [
                    "Task A must be completed before Task B.",
                    "Task C and Task D cannot be scheduled in consecutive time slots.",
                    "Task B requires 2 time slots to complete.",
                    "Each task must be assigned exactly one time slot.",
                    "No time slot should be left empty."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "employees" in t:
            return f"""Create an optimized work schedule for the following employees based on the given constraints:

Employees: {', '.join(t['employees'])}
Shifts: {', '.join(t['shifts'])}
Constraints: {', '.join(t['constraints'])}

Submit your schedule as a plain text string in the format:

Employee: Shift, Shift, Shift, Shift, Shift
"""
        else:
            return f"""Create an optimized task schedule based on the given constraints:

Tasks: {', '.join(t['tasks'])}
Time Slots: {', '.join(t['time_slots'])}
Constraints: {', '.join(t['constraints'])}

Submit your schedule as a plain text string in the format:

Task: Time Slot, Task: Time Slot, Task: Time Slot, Task: Time Slot
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The schedule must satisfy all given constraints.",
            "The schedule must be logically coherent and practical.",
            "The schedule should be optimized to balance the workload fairly among employees or time slots."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
