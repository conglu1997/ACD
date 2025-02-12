class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "A man says 'I always lie.' Is he telling the truth or lying? Explain your reasoning."},
            "2": {"puzzle": "In a town, there is a barber who shaves everyone who does not shave themselves. Does the barber shave himself? Explain your reasoning."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and solve the following logical puzzle or paradox. Provide a clear and logical explanation for your solution.

Puzzle:
{t['puzzle']}

Your response should include:
1. A clear interpretation of the puzzle or paradox.
2. A logical solution or explanation.
3. Any assumptions or reasoning steps you used to arrive at your solution.
4. Ensure your explanation is detailed, coherent, and logically sound."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should interpret the puzzle or paradox correctly.",
            "The response should provide a logical solution or explanation.",
            "The response should include any assumptions or reasoning steps used to arrive at the solution.",
            "The explanation should be detailed, coherent, and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
