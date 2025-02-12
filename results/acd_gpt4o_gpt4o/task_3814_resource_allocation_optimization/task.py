class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "resources": {"A": 10, "B": 20, "C": 30},
                "tasks": {"Task1": {"A": 3, "B": 5}, "Task2": {"A": 2, "C": 7}, "Task3": {"B": 10, "C": 4}},
                "objective": "Minimize the total number of resources used while completing all tasks."
            },
            "2": {
                "resources": {"X": 15, "Y": 25},
                "tasks": {"TaskA": {"X": 4, "Y": 6}, "TaskB": {"X": 5, "Y": 8}, "TaskC": {"X": 3, "Y": 9}},
                "objective": "Maximize the number of tasks completed without exceeding resource limits."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to optimize the allocation of resources based on the given constraints and objectives. You are provided with a set of resources and a list of tasks, each requiring certain amounts of these resources. Your objective is to {t['objective']}.

Resources: {t['resources']}
Tasks: {t['tasks']}

Provide your solution in plain text format, detailing the allocation of resources to each task and explaining how your allocation meets the objective. Ensure that no resource limits are exceeded and that all tasks are completed where possible. Format your response as follows:\n\nSolution:\nTask1: A=3, B=5\nTask2: A=2, C=7\nTask3: B=10, C=4\nExplanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The allocation should be efficient and meet the specified objective.",
            "All tasks should be completed without exceeding resource limits.",
            "The solution should be clearly explained and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
