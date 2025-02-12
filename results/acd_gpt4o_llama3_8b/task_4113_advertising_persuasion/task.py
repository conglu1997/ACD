class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "product": "A new eco-friendly reusable water bottle",
                "requirements": "Highlight its environmental benefits, durability, and sleek design. Appeal to environmentally conscious consumers."
            },
            "2": {
                "advertisement": "Introducing our new fitness app! Track your workouts, monitor your progress, and achieve your fitness goals with personalized plans. Join our community of fitness enthusiasts and start your journey to a healthier you today!",
                "analysis_criteria": "Effectiveness in conveying benefits, clarity, and persuasiveness."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'product' in t:
            return f"""Generate a compelling advertisement for the following product:

Product: {t['product']}

Requirements: {t['requirements']}

Your advertisement should be engaging, persuasive, and clearly highlight the specified features and benefits. Submit your ad as a plain text string in the following format:

Advertisement: [Your advertisement here]"""
        else:
            return f"""Analyze the effectiveness of the following advertisement:

Advertisement: {t['advertisement']}

Your analysis should address the following criteria:
1. Effectiveness in conveying the benefits of the product or service.
2. Clarity of the message.
3. Persuasiveness of the content.

Submit your analysis as a plain text string in the following format:

Analysis: [Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'product' in t:
            validation_criteria = [
                "The advertisement should be engaging and persuasive.",
                "The advertisement should clearly highlight the specified features and benefits."]
        else:
            validation_criteria = [
                "The analysis should address the effectiveness in conveying the benefits of the product or service.",
                "The analysis should address the clarity of the message.",
                "The analysis should address the persuasiveness of the content."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
