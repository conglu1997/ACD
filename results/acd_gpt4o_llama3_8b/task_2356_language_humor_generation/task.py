class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "words": ["tuna", "calendar"],
                "explanation": "Generate a pun using the word 'tuna' and another using the word 'calendar'. Explain why each pun is humorous."
            },
            "2": {
                "words": ["bicycle", "lamp"],
                "explanation": "Generate a pun using the word 'bicycle' and another using the word 'lamp'. Explain why each pun is humorous."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a pun using each of the provided words and explain why each pun is humorous. Ensure that your puns are creative and that the explanations clearly describe the wordplay or cultural context behind the humor. Each explanation should be at least 20 words long.\n\nWords:\n- {t['words'][0]}\n- {t['words'][1]}\n\nFormat your response as follows:\n1. Pun for '{t['words'][0]}': [Your pun]\n   Explanation: [Your explanation]\n2. Pun for '{t['words'][1]}': [Your pun]\n   Explanation: [Your explanation]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a pun for each provided word.",
            "The explanations should clearly describe the wordplay or cultural context behind the humor.",
            "Each explanation should be at least 20 words long.",
            "The puns should be creative and demonstrate an understanding of language nuances."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
