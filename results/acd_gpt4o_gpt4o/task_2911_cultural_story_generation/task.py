class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "culture": "Japanese",
                "historical_context": "Edo period",
                "elements": "samurai, tea ceremony, cherry blossoms"
            },
            "2": {
                "culture": "Ancient Greek",
                "historical_context": "Classical period",
                "elements": "philosopher, agora, olive grove"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a culturally appropriate short story based on the given cultural elements and historical context. Ensure that the story is respectful and accurately represents the cultural and historical setting. The story should be engaging and coherent, integrating all the provided elements in a meaningful way.\n\nCulture: {t['culture']}\nHistorical Context: {t['historical_context']}\nElements: {t['elements']}\n\nProvide your response in plain text format and ensure it is between 300 to 500 words."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should accurately reflect the given cultural and historical context.",
            "The story should integrate all provided elements in a meaningful way.",
            "The story should be engaging and coherent.",
            "The story should be respectful of the culture it represents."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
