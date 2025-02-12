class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"product": "eco-friendly water bottle", "target_audience": "young professionals"},
            "2": {"product": "smart home security system", "target_audience": "families with children"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a persuasive advertisement for the following product:

Product: {t['product']}
Target Audience: {t['target_audience']}

Your advertisement should include the following elements:
1. A catchy headline.
2. A description of the product's key features and benefits.
3. A call to action.

Submit your advertisement as a plain text string in the following format:

Headline: [Your catchy headline]
Description: [Your description of the product's key features and benefits]
Call to Action: [Your call to action]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The advertisement should include a catchy headline.", "The advertisement should describe the product's key features and benefits.", "The advertisement should include a clear call to action."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
