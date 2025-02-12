class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Why renewable energy is essential for the future.", "persuasive_text": "Renewable energy sources like solar and wind are crucial for reducing our dependence on fossil fuels. They help mitigate climate change, reduce air pollution, and create sustainable jobs. Investing in renewable energy is an investment in our planet's future."},
            "2": {"topic": "The importance of a balanced diet for maintaining health.", "persuasive_text": "A balanced diet is essential for maintaining good health. It provides the necessary nutrients for our bodies to function properly, boosts our immune system, and helps prevent chronic diseases. By eating a variety of foods in the right proportions, we can ensure our bodies get the nourishment they need."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        persuasive_text = t.get("persuasive_text", "")
        if persuasive_text:
            return f"""Evaluate the persuasiveness of the following text on the topic '{topic}':\n\n{persuasive_text}\n\nYour evaluation should include an analysis of the rhetorical techniques used, the strength of the arguments, and any improvements that could be made. Submit your evaluation as a plain text string in the following format:\n\nEvaluation: [Your evaluation]"""
        else:
            return f"""Generate a persuasive text on the topic '{topic}'. Your text should include strong arguments, use rhetorical techniques, and be compelling to the reader. Submit your persuasive text as a plain text string in the following format:\n\nPersuasive Text: [Your text]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "persuasive_text" in t:
            criteria = ["The evaluation should include an analysis of rhetorical techniques.", "The evaluation should assess the strength of the arguments.", "The evaluation should suggest improvements."]
        else:
            criteria = ["The text should be persuasive and compelling.", "The text should include strong arguments.", "The text should use rhetorical techniques."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
