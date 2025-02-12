class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"product": "A new smart refrigerator that includes features like voice control, automatic restocking, and energy efficiency."},
            "2": {"service": "A premium personal training service that offers customized workout plans, nutrition advice, and 24/7 support."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "product" in t:
            return f"""Write a persuasive product description for the following product:

{t["product"]}

Your product description should highlight the key features and benefits, appeal to the target audience's needs and desires, and include a strong call to action. Ensure that your description is engaging, convincing, and well-structured. The description should be no more than 200 words. Submit your response as a plain text string."""
        else:
            return f"""Write a persuasive sales pitch for the following service:

{t["service"]}

Your sales pitch should highlight the key features and benefits, appeal to the target audience's needs and desires, and include a strong call to action. Ensure that your pitch is engaging, convincing, and well-structured. The sales pitch should be no more than 200 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description/pitch should highlight key features and benefits.", "The description/pitch should appeal to the target audience's needs and desires.", "The description/pitch should include a strong call to action.", "The description/pitch should be engaging, convincing, and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
