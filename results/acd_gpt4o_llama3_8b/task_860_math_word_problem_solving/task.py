class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "If a train travels at a speed of 60 miles per hour and takes 3 hours to reach its destination, how far did it travel?"},
            "2": {"problem": "A farmer has 20 apples. He decides to distribute them among his 4 children equally. How many apples does each child get?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"""Solve the following word problem:

{problem}

Provide your solution as a single numerical answer. Your answer should be a plain number without units or additional text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        tasks = TaskFamily.get_tasks()
        if t == tasks["1"]:
            criteria = ["The answer should be 180."]
        elif t == tasks["2"]:
            criteria = ["The answer should be 5."]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
