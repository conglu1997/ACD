class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "setup": "Why don't scientists trust atoms?"
            },
            "2": {
                "setup": "Why did the scarecrow win an award?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous punchline for the following setup and explain why it is funny:

Setup: {t['setup']}

Ensure your punchline is original, creative, and clearly related to the setup. After generating the punchline, provide a detailed explanation of why it is funny. Submit your response as a plain text string with the following format:

Punchline: [Your punchline here]
Explanation: [Your explanation here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The punchline should be original, creative, and clearly related to the setup.", "The explanation should detail why the punchline is funny, discussing elements such as incongruity, wordplay, or cultural references."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
