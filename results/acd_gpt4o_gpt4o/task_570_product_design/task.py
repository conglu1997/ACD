class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Design a new kitchen gadget that helps in meal preparation. The gadget should be easy to use, affordable, and cater to both novice and experienced cooks."},
            "2": {"criteria": "Design an innovative piece of wearable technology for fitness enthusiasts. The product should track various fitness metrics, be comfortable to wear, and have a unique selling point."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a new product based on the given criteria:

Criteria: {t["criteria"]}

Provide a detailed description of your product, including the following elements:

1. Product Name
2. Features: List and describe the main features of the product.
3. Target Audience: Identify who would benefit most from this product.
4. Use Cases: Describe potential scenarios where this product would be useful.
5. Unique Selling Point: Explain what sets this product apart from others on the market.

Ensure that your design is original, creative, and practical. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The product design should be detailed and original.",
            "The features should be practical and well-explained.",
            "The target audience should be clearly identified.",
            "The use cases should be realistic and relevant.",
            "The unique selling point should be compelling and distinct."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
