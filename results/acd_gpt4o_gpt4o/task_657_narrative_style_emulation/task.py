class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Describe a stormy night", "style": "Edgar Allan Poe"},
            "2": {"prompt": "A day in a futuristic city", "style": "Isaac Asimov"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a narrative passage based on the following prompt and in the specified style:

Prompt: {t['prompt']}
Style: {t['style']}

Ensure that your passage is coherent, captures the essence of the prompt, and closely follows the stylistic elements of the specified author or genre. Provide your narrative in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The passage should be coherent.",
            "The passage should capture the essence of the prompt.",
            "The passage should closely follow the stylistic elements of the specified author or genre."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
