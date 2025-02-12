class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "If a train travels at a speed of 60 miles per hour for 3 hours, how far will it have traveled?", "criteria": "distance, speed, and time"},
            "2": {"problem": "A rectangle has a length of 10 units and a width of 5 units. What is its area?", "criteria": "area, length, and width"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves understanding and generating mathematical problems:

1. Interpret the following mathematical problem and provide a clear and concise solution.

Problem: {t['problem']}

Please provide your solution in the following format:
- Solution: [Your solution]

2. Generate a new mathematical problem based on the given criteria.

Criteria: {t['criteria']}

Ensure that your problem is original, solvable, and adheres to the given criteria. Provide the generated problem in the following format:
- Problem: [Your problem]

Both parts of the task are equally important. Make sure your responses are clear and detailed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Define criteria for evaluation
        criteria = [
            "The solution should correctly solve the given problem.",
            "The generated problem should be original and adhere to the given criteria.",
            "The generated problem should be solvable and clearly stated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
