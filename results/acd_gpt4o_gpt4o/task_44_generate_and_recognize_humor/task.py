class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the scarecrow win an award?"},
            "2": {"statement": "Parallel lines have so much in common. It’s a shame they’ll never meet."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a joke based on the following prompt:

{t['prompt']}

Ensure the joke is humorous, concise, and relevant to the prompt. The joke should be original and not a repetition of common jokes. Provide your joke in plain text format."""
        else:
            instructions = f"""Your task is to recognize the humorous intent in the following statement and explain why it is funny:

{t['statement']}

Provide a clear explanation that demonstrates an understanding of the humor in the statement. Your explanation should be concise and to the point. Provide your explanation in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = ["The response should be a joke that is relevant to the given prompt.", "The joke should be original, humorous, and make sense."]
        else:
            criteria = ["The explanation should demonstrate an understanding of the humorous intent in the statement.", "The explanation should be clear, concise, and to the point."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
