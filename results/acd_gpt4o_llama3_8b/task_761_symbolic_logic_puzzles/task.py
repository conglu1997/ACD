class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "If P implies Q and Q implies R, does P imply R? Justify your answer using symbolic logic."},
            "2": {"puzzle": "Given the following premises: (1) If it rains, then the ground is wet. (2) If the ground is wet, then the flowers bloom. (3) It is raining. Does it follow that the flowers bloom? Prove your answer using symbolic logic."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following symbolic logic puzzle:

{t["puzzle"]}

Provide a detailed justification of your answer using symbolic logic. Ensure that your reasoning is clear and follows the principles of logical inference. Submit your response as a plain text string in the following format:

Answer: [Your answer here]
Justification: [Your detailed justification here]

Example Response:
Answer: Yes
Justification: Given P -> Q and Q -> R, we can use the transitivity of implication to conclude that P -> R. Since both premises hold, the conclusion P -> R logically follows."

Example Response:
Answer: Yes
Justification: Given (1) If it rains, then the ground is wet, (2) If the ground is wet, then the flowers bloom, and (3) It is raining, we can use the transitivity of implication to conclude that the flowers bloom. Since all premises hold, the conclusion that the flowers bloom logically follows."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should use symbolic logic correctly.",
            "The reasoning should be clear and logically sound.",
            "The answer should correctly address the puzzle's question."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
