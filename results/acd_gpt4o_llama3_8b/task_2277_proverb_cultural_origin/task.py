class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "proverb": "A stitch in time saves nine."
            },
            "2": {
                "proverb": "The early bird catches the worm."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the country or culture of origin for the following proverb and explain its meaning:

Proverb: {t['proverb']}

Your response should include:
1. The country or culture of origin.
2. An explanation of the proverb's meaning.

Note: Avoid generic or vague explanations. Be specific and detailed in your response.

Submit your response as a plain text string in the following format:
- Origin: [Country or Culture]
- Meaning: [Explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include the correct country or culture of origin.",
            "The explanation of the proverb's meaning should be accurate and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
