class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the math book look sad?"},
            "2": {"prompt": "Why don't scientists trust atoms?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a pun based on the following prompt and explain the humor behind it:

Prompt: {t['prompt']}

Ensure that the pun is funny, coherent, and appropriate. The explanation should clearly describe the wordplay and why it is humorous. Provide your response in the following format:

Pun: [Your pun]
Explanation: [Your explanation]

Example:
Prompt: Why did the scarecrow win an award?
Pun: Because he was outstanding in his field.
Explanation: The pun plays on the double meaning of 'outstanding'—both as being exceptionally good and literally standing out in a field, which is where scarecrows are placed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a pun based on the given prompt.", "The explanation should clearly describe the wordplay and why it is humorous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
