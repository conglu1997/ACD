class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Create a character who is a retired detective with a mysterious past."},
            "2": {"prompt": "Create a character who is a young scientist discovering a groundbreaking invention."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed fictional character based on the following prompt:

{t["prompt"]}

Your response should include:
1. The character's name, age, and physical description.
2. A brief backstory that explains their past and how they got to their current situation.
3. Key personality traits and any notable quirks or habits.
4. A description of the character's current goals or motivations.

Ensure your character is well-developed, coherent, and fits the given prompt. Format your response in plain text without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the character's name, age, and physical description.",
            "The response should include a brief backstory.",
            "The response should describe key personality traits and notable quirks or habits.",
            "The response should describe the character's current goals or motivations.",
            "The character should be well-developed, coherent, and fit the given prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
