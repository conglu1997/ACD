class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate a pun involving a fruit and a job."},
            "2": {"prompt": "Explain the humor in the following pun: 'I used to be a baker, but I couldn't make enough dough.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task involves two parts: generating puns and interpreting humor.

Task 1: Generate a pun based on the given prompt. Ensure that your pun is creative and humorous. Provide your response in plain text format.
Prompt: {prompt}

Task 2: Explain the humor in the provided pun. Ensure that your explanation is clear and captures the essence of the pun. Provide your response in plain text format.
Prompt: {prompt}""".format(prompt=t["prompt"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The pun should be creative and humorous."] if "Generate" in instructions else ["The explanation should clearly capture the essence of the pun."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
