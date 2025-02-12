class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "product": "Smartphone with a 6.5-inch display, 128GB storage, 12MP camera, and a long-lasting battery.",
                "additional_details": "Supports 5G connectivity, available in black and blue colors, and comes with a one-year warranty."},
            "2": {
                "product": "Wireless noise-cancelling headphones with 30-hour battery life, built-in microphone, and comfortable over-ear design.",
                "additional_details": "Available in black and white colors, supports Bluetooth 5.0, and includes a travel case."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a compelling and informative product description based on the provided product details.

Product:
{t['product']}

Additional Details:
{t['additional_details']}

Ensure the description highlights the key features, appeals to potential buyers, and is engaging and persuasive. The description should be between 100 to 150 words.
Submit your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should highlight the key features of the product.",
                   "The description should be engaging and persuasive.",
                   "The description should be between 100 to 150 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
