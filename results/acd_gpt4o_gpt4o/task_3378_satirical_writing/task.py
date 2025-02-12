class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a satirical news article about a fictional tech company's latest product release."},
            "2": {"prompt": "Write a satirical opinion piece on the current state of social media and its impact on society."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a satirical piece based on the following prompt:

Prompt: {t['prompt']}

Your satirical piece should include:
1. Humor and irony that clearly convey the satirical nature of the piece.
2. Cultural references and knowledge relevant to the topic.
3. A coherent and engaging narrative.

Ensure your satire is clear and effectively communicates the intended humor and irony. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The piece should include humor and irony.", "The piece should make relevant cultural references.", "The narrative should be coherent and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
