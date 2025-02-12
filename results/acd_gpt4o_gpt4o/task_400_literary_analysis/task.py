class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."},
            "2": {"text": "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """You are provided with a short passage from a piece of literature. Your task is to perform the following:
1. Generate a brief summary of the passage (1-2 sentences).
2. Identify and explain the main theme of the passage (1-2 sentences).

Passage:
{t['text']}

Example response format:
1. Summary: [Your summary here]
2. Theme: [Your theme analysis here]

Ensure that your summary captures the main events or descriptions accurately, and your theme analysis correctly identifies and explains the main theme of the passage."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should accurately capture the main events or descriptions in the passage.",
            "The thematic analysis should correctly identify and explain the main theme of the passage."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
