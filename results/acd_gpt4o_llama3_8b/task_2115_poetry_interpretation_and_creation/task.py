class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "poem": "Shall I compare thee to a summer's day? / Thou art more lovely and more temperate: / Rough winds do shake the darling buds of May, / And summer's lease hath all too short a date;",
                "theme": "nature",
                "structure": "sonnet"
            },
            "2": {
                "poem": "Once upon a midnight dreary, while I pondered, weak and weary, / Over many a quaint and curious volume of forgotten lore—",
                "theme": "mystery",
                "structure": "rhymed couplets"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following poem and create a new poem with the specified theme and structure.

Poem: {t['poem']}

Theme: {t['theme']}
Structure: {t['structure']}

Your response should include:
1. An interpretation of the given poem, explaining its meaning and any notable literary devices.
2. A new poem that adheres to the specified theme and structure. For example, if the structure is a sonnet, ensure it follows the 14-line format with an appropriate rhyme scheme (e.g., ABABCDCDEFEFGG for a Shakespearean sonnet).

Submit your response as a plain text string in the following format:
Interpretation: [Your interpretation]
New Poem: [Your new poem]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should accurately explain the meaning of the given poem and identify notable literary devices.",
            "The new poem should adhere to the specified theme and structure, including the correct format and rhyme scheme for the structure (e.g., 14 lines and ABABCDCDEFEFGG rhyme scheme for a Shakespearean sonnet)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
