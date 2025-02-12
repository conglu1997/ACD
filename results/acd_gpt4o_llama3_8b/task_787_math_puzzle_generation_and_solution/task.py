class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Create a mathematical puzzle that involves a sequence of numbers with a hidden pattern. Provide the puzzle along with its solution and a detailed explanation of the pattern."},
            "2": {"prompt": "Solve the following mathematical puzzle: 2, 4, 8, 16, ? Provide the solution and a detailed explanation of the reasoning behind your answer."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task:

{t['prompt']}

For Task 1, provide a clear description of the puzzle, its solution, and an explanation of the hidden pattern. For Task 2, provide the solution to the puzzle and a detailed explanation of the reasoning behind your answer. Ensure that your response is well-reasoned, coherent, and demonstrates a deep understanding of mathematical principles. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['prompt'].startswith("Create"):
            criteria = ["The response should include a clear description of the puzzle.", "The response should include the solution to the puzzle.", "The puzzle should involve a sequence of numbers with a hidden pattern."]
        else:
            criteria = ["The response should include the correct solution to the puzzle.", "The response should include a detailed explanation of the reasoning behind the solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
