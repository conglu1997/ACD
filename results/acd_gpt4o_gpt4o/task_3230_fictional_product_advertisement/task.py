class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_description": "Design a fictional eco-friendly gadget for home use and write a persuasive advertisement for it."},
            "2": {"task_description": "Design a fictional educational toy for children and write a persuasive advertisement for it."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a fictional product and write a persuasive advertisement for it.

Task: {t['task_description']}

Instructions:
1. Create a detailed description of the fictional product, including its features, benefits, and target audience.
2. Write a persuasive advertisement that highlights the product's unique selling points.
3. Ensure the advertisement is engaging, clear, and compelling.
4. The advertisement should be coherent and cover all necessary aspects to persuade the target audience.
5. Use appropriate marketing language and techniques.

Your response should be structured as follows:
Product Description: [Detailed description of the product]
Advertisement: [Persuasive advertisement text]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The product description should be detailed and imaginative.", "The advertisement should be persuasive and engaging.", "The advertisement should highlight the product's unique selling points.", "The overall response should be coherent and compelling."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
