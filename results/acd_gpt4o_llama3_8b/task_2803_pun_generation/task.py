class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "word_or_phrase": "bicycle"
            },
            "2": {
                "word_or_phrase": "calendar"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a pun based on the following word or phrase:

Word or Phrase: {t['word_or_phrase']}

Your response should include:
1. The pun.
2. A brief explanation of the wordplay used in the pun.

Ensure that the pun is original, humorous, and demonstrates a creative use of the given word or phrase. Submit your response as a plain text string in the following format:
- Pun: [Your pun]
- Explanation: [Your explanation]

Example:
Word or Phrase: "eggs"
- Pun: "Eggsciting news!"
- Explanation: This pun plays on the word "exciting" by substituting "egg" to make a humorous statement about news involving eggs.

Note: Originality and creativity are highly valued in your response. Avoid using common or overused puns.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The pun should be original.",
            "The pun should be humorous.",
            "The explanation should clearly describe the wordplay used.",
            "The pun should be contextually appropriate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
