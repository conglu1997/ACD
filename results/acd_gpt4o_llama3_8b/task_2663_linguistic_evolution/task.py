class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ancient_language": "Old English",
                "word": "cyning"
            },
            "2": {
                "ancient_language": "Latin",
                "word": "amicus"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following word in {t['ancient_language']}, analyze its evolution into its modern counterpart. Your response should include:

1. The original meaning and context of the word, including its use in sentences if possible.
2. A detailed analysis of the phonetic changes over time, including specific sound shifts.
3. A detailed analysis of the semantic changes over time, including shifts in meaning and usage.
4. The modern English equivalent of the word.
5. A brief explanation of any cultural or historical factors that influenced the changes, including relevant events or societal shifts.

Submit your response as a plain text string in the following format:

Ancient Language: {t['ancient_language']}

Original Word: {t['word']}

Original Meaning: [Your analysis]
Phonetic Changes: [Your analysis]
Semantic Changes: [Your analysis]
Modern English Equivalent: [Your analysis]
Cultural/Historical Factors: [Your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the original meaning and context of the word, including its use in sentences if possible.",
            "The response should provide a detailed analysis of the phonetic changes, including specific sound shifts.",
            "The response should provide a detailed analysis of the semantic changes, including shifts in meaning and usage.",
            "The response should provide the correct modern English equivalent of the word.",
            "The response should explain relevant cultural or historical factors influencing the changes, including relevant events or societal shifts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0