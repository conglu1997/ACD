class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You are given two ropes. Each rope takes exactly 1 hour to burn from one end to the other. However, the ropes do not burn at a constant rate. How can you measure exactly 45 minutes using these two ropes?"},
            "2": {"puzzle": "You have a 3-liter jug and a 5-liter jug, both unmarked. How can you measure exactly 4 liters of water using these two jugs?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical puzzle:\n\nPuzzle: {t['puzzle']}\n\nProvide your solution in plain text format, explaining your reasoning and steps clearly. Ensure your explanation is detailed and covers all the steps you took to arrive at the solution."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['puzzle'].startswith('You are given two ropes'):
            criteria = ["The solution should involve burning the ropes in a specific way to measure exactly 45 minutes."]
        else:
            criteria = ["The solution should describe a method to measure exactly 4 liters of water using the two jugs."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
