class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dialect": "Scottish English",
                "scenario": "Write a dialogue between two friends meeting at a local pub in Edinburgh. Ensure the dialogue reflects the Scottish English dialect, including appropriate vocabulary, grammar, and cultural references."
            },
            "2": {
                "dialect": "African American Vernacular English (AAVE)",
                "scenario": "Write a narrative describing a family gathering in an urban neighborhood. Ensure the narrative reflects AAVE, including appropriate vocabulary, grammar, and cultural references."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a {t['dialect']} dialogue or narrative based on the following scenario. Ensure linguistic accuracy and cultural appropriateness.\n\nScenario:\n{t['scenario']}\n\nFormat your response in plain text.\nResponse: [Your dialogue or narrative]\n\nNote: Pay close attention to the dialect-specific vocabulary, grammar, and cultural nuances. Your response should convincingly reflect the specified dialect and context."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately reflect the specified dialect, including appropriate vocabulary and grammar.",
            "The response should be culturally appropriate and coherent.",
            "The response should convincingly reflect the specified dialect and context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
