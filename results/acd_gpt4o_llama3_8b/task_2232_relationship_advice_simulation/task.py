class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Your friend feels neglected because you have been spending a lot of time with your new partner. How do you address your friend's feelings and maintain both relationships?"
            },
            "2": {
                "scenario": "A colleague frequently interrupts you during meetings, making it difficult for you to express your ideas. How do you handle this situation while maintaining a professional relationship?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following scenario, provide advice on how to handle the situation. Your advice should demonstrate empathy, understanding of the involved parties' perspectives, and offer practical solutions.

Scenario: {t['scenario']}

Submit your advice as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The advice should demonstrate empathy.",
            "The advice should show an understanding of the involved parties' perspectives.",
            "The advice should offer practical solutions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
