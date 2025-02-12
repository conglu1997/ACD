class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"passage": "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.", "author": "George Orwell"},
            "2": {"passage": "In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since. 'Whenever you feel like criticizing anyone,' he told me, 'just remember that all the people in this world haven't had the advantages that you've had.'", "author": "F. Scott Fitzgerald"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following literary passage and write a continuation in the style of the original author. Ensure your continuation maintains the same tone, style, and voice as the original passage. Submit your response as a plain text string in the following format:

Original Passage: {t['passage']}

Continuation: [Your Continuation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The continuation should maintain the same tone, style, and voice as the original passage.",
            "The response should follow the format: Original Passage: [Original Passage] Continuation: [Your Continuation]"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
