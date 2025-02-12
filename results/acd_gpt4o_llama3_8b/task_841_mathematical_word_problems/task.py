class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "John has three times as many apples as Mary. If Mary has 5 apples, how many apples do they have together?"
            },
            "2": {
                "problem": "A car travels at a speed of 60 km/h. How long will it take to cover a distance of 180 km?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"""Solve the following mathematical word problem and explain your solution step-by-step. Problem: {problem}\n
Submit your solution and explanation as a plain text string in the following format: 'Solution: [Your solution]\nExplanation: [Your step-by-step explanation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be correct.", "The explanation should clearly describe the steps taken to solve the problem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
