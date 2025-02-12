class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "product_brief": "Develop a new wearable fitness device that not only tracks physical activity but also monitors mental health indicators. Provide a detailed description of the product, including its features, target audience, and how it stands out in the market."
            },
            "2": {
                "product_brief": "Create an innovative kitchen appliance that helps home cooks with meal planning and preparation. Describe the product's main features, target audience, and potential impact on home cooking."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a new product idea based on the following brief. Provide a detailed description of the product, including its features, target audience, and potential market impact.

Product Brief: '{t['product_brief']}'

Ensure your description is clear, coherent, and demonstrates a solid understanding of both the creative and practical aspects of product design. Submit your response as a plain text string in the following format:

Product Description: [Your detailed description]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The product description must be clear and coherent.",
            "The product features must be well-defined.",
            "The target audience must be clearly identified.",
            "The potential market impact must be discussed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
