class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "technology"},
            "2": {"theme": "environment"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        instructions = f"""Your task is to create a modern proverb that encapsulates wisdom related to the theme of '{theme}'. The proverb should be concise, memorable, and reflect contemporary understanding of the theme. Additionally, provide an explanation of the meaning behind the proverb. Structure your response as follows:

Proverb: [Your modern proverb]
Explanation: [Explanation of the proverb's meaning]

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proverb should be concise and memorable.",
            "The proverb should reflect contemporary understanding of the theme.",
            "The explanation should clearly convey the meaning of the proverb."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
