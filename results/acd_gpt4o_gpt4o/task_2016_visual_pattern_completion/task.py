class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": ["*", "**", "***", "****"]},
            "2": {"sequence": ["1", "22", "333", "4444"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to predict the next pattern in the following sequence of visual patterns represented in ASCII art:

Sequence: {t['sequence']}

Analyze the given patterns and provide the next pattern in the sequence. Ensure that your prediction follows the same logical progression as the given sequence.

Provide your response in plain text format as the next pattern in the sequence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        correct_answer = ''.join([str(len(t['sequence']) + 1)] * (len(t['sequence']) + 1)) if t['sequence'][0].isdigit() else '*' * (len(t['sequence']) + 1)
        criteria = [f"The response should match the logical progression of the sequence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) and submission.strip() == correct_answer else 0.0
