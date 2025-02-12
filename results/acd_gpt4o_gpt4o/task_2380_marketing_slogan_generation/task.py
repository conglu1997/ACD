class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "product_name": "EcoClean",
                "product_description": "A new line of environmentally friendly cleaning products that use natural ingredients to effectively clean various surfaces without harming the environment."
            },
            "2": {
                "product_name": "TechWave",
                "product_description": "An innovative smartwatch that not only tracks your fitness metrics but also offers advanced features such as sleep monitoring, contactless payments, and seamless integration with your smartphone."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a catchy and persuasive marketing slogan or tagline for the following product based on its description.

Product Name: {t['product_name']}

Product Description: {t['product_description']}

Ensure that your slogan is concise, memorable, and effectively communicates the key features and benefits of the product."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The slogan is catchy and memorable.",
            "The slogan effectively communicates the key features and benefits of the product.",
            "The slogan is concise."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
