class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"expression": "2x + 3 = 7"},
            "2": {"expression": "3(y - 2) = 9"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given mathematical expression and perform the following steps:

1. Simplify the given expression to solve for the variable.
2. Generate a new, equivalent expression that has the same solution.
3. Solve the new expression to verify that it is equivalent to the original.

Expression: {t['expression']}

Provide your response in the following format:

Original Solution: [Solution of the original expression]
New Expression: [Your new equivalent expression]
New Solution: [Solution of the new expression]

Example:
Expression: x + 2 = 5
Original Solution: x = 3
New Expression: 2x - 3 = 3
New Solution: x = 3

Ensure that your new expression is mathematically equivalent to the original and that the solutions match. Avoid trivial transformations like adding zero, multiplying by one, or making superficial changes like rearranging terms without affecting the overall structure. Non-trivial transformations include operations like distributing terms, factoring, or using inverse operations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The original solution should correctly solve the given expression.", 
            "The new expression should be mathematically equivalent to the original.", 
            "The new solution should match the original solution.",
            "The new expression should not be a trivial transformation (e.g., adding zero, multiplying by one, or superficial changes)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
