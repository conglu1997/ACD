class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "black holes",
                "audience": "high school students"
            },
            "2": {
                "phenomenon": "quantum entanglement",
                "audience": "general public"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "You will be given a complex scientific phenomenon and an audience type. Your task is to explain the phenomenon in a way that is accessible and understandable to the given audience. Your explanation should be clear, engaging, and appropriately detailed for the audience."
        instructions += f"\nPhenomenon: {t['phenomenon']}"
        instructions += f"\nAudience: {t['audience']}"
        instructions += "\nSubmit your explanation as a plain text string."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be accurate and scientifically correct.",
            "The explanation should be clear and understandable to the specified audience.",
            "The explanation should be engaging and appropriately detailed for the audience.",
            "The explanation should simplify the complex phenomenon without losing essential details.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
