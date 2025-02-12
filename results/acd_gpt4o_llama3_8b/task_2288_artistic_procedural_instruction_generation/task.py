class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "project": "Create a watercolor painting of a landscape."
            },
            "2": {
                "project": "Craft a handmade greeting card using mixed media techniques."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate detailed, step-by-step instructions for the following artistic project. Ensure your instructions are clear, comprehensive, and include creative advice. The instructions should allow someone with no prior experience to successfully complete the project. Include any necessary materials, techniques, and tips for best results. Submit your instructions as a plain text string.\n\nProject: {t['project']}\n\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The instructions should be clear and detailed.",
            "The instructions should cover all necessary steps to complete the project.",
            "The instructions should include any necessary materials, techniques, and creative tips for best results."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
