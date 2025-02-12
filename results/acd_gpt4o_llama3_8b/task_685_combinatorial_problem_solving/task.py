class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "In how many ways can you arrange the letters of the word 'COMBINATORIAL'?"
            },
            "2": {
                "problem": "A committee of 5 members is to be formed from a group of 8 men and 5 women. In how many ways can this be done if the committee must contain at least 2 women?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following combinatorial problem:

Problem: {t['problem']}

Your response should include:
1. A clear explanation of the steps you took to solve the problem.
2. The final answer.

Submit your response as a plain text string in the following format:
- Solution: [Your explanation here]
- Answer: [Your final answer here]

Ensure your explanation is detailed and logically sequenced. Make sure to follow the specified format exactly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should clearly outline the steps taken to solve the problem.",
            "The answer should be correct based on the problem statement.",
            "The response should follow the specified format precisely.",
            "The explanation should be logical and thorough."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
