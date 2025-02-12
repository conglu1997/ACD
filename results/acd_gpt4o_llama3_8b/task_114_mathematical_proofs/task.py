class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Prove that the sum of two even numbers is always even."},
            "2": {"problem": "Prove that the square root of 2 is irrational."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given problem:

Problem: {t['problem']}

Generate a mathematical proof to solve the problem. Your proof should follow these guidelines:
1. Clearly state the problem and any assumptions.
2. Use appropriate mathematical notation and terminology.
3. Ensure that each step follows logically from the previous one.
4. Provide justification for each step, referencing relevant mathematical principles or theorems.
5. Conclude by summarizing how the proof addresses the problem statement.

Submit your proof as a plain text string, ensuring clarity and coherence in your explanation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The proof should clearly state the problem and any assumptions.", "Appropriate mathematical notation and terminology should be used.", "Each step should follow logically from the previous one.", "Each step should be justified with relevant mathematical principles or theorems.", "The conclusion should summarize how the proof addresses the problem statement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
