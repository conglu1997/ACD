class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["The sum of two numbers is 10.", "The product of the same two numbers is 24."], "query": "What are the two numbers?"},
            "2": {"premises": ["A number is three times another number.", "The sum of these two numbers is 16."], "query": "What are the two numbers?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical logic puzzle based on the given premises:

Premises: {', '.join(t['premises'])}

Query: {t['query']}

Provide your answer as a plain text string in the following format:
Number 1: [First number]
Number 2: [Second number]
Ensure your solution is logically consistent with the premises provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
