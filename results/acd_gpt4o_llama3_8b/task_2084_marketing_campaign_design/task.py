class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"product": "Eco-friendly Water Bottle", "features": ["reusable", "BPA-free", "keeps drinks cold for 24 hours"]},
            "2": {"product": "Smart Fitness Tracker", "features": ["heart rate monitor", "sleep tracking", "GPS"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a comprehensive marketing campaign for the following product: '{t["product"]}' with features '{', '.join(t['features'])}'. Your campaign should include the following components:

1. Target Audience: Identify and describe the primary target audience for the product.
2. Key Messages: Develop at least three key messages that effectively communicate the benefits and features of the product to the target audience.
3. Promotional Strategies: Outline at least three promotional strategies to reach and engage the target audience. Consider using a mix of digital and traditional marketing channels.

Ensure that your campaign is coherent, innovative, and feasible. Submit your response as a plain text string in the following format:

1. Target Audience: [Your description here]
2. Key Messages: [Your key messages here]
3. Promotional Strategies: [Your strategies here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The campaign should include a clearly identified target audience.", "The key messages should effectively communicate the product's features and benefits.", "The promotional strategies should be innovative and feasible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
