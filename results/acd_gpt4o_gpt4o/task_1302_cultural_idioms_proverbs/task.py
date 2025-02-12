class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "A bird in the hand is worth two in the bush.", "culture": "English"},
            "2": {"idiom": "Khi nước lên, thuyền lên.", "culture": "Vietnamese"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following idiomatic expression or proverb from the given culture. Explain its meaning and provide an equivalent expression in English if applicable.

Idiom/Proverb: {t['idiom']}
Culture: {t['culture']}

Ensure your interpretation is clear and accurately conveys the meaning of the expression within its cultural context. Provide your response in plain text format as follows:

Interpretation: <Your interpretation>
Equivalent Expression: <Equivalent expression in English (if any)>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should accurately convey the meaning of the idiom or proverb.", "The equivalent expression in English should be appropriate and relevant (if provided)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
