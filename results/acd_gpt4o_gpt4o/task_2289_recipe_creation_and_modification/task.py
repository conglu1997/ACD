class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "rice", "broccoli", "soy sauce", "garlic", "ginger"], "dietary_restriction": "gluten-free"},
            "2": {"ingredients": ["tofu", "quinoa", "spinach", "tomatoes", "olive oil", "basil"], "dietary_restriction": "vegan"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a cooking recipe based on the following ingredients:

{', '.join(t['ingredients'])}

Then, modify the recipe to accommodate the following dietary restriction: {t['dietary_restriction']}.

Ensure that the recipe is clear, detailed, and includes all necessary steps and measurements. Provide the original recipe and the modified recipe as two separate sections in plain text format with the headers 'Original Recipe' and 'Modified Recipe'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the original recipe and the modified recipe as two separate sections with the headers 'Original Recipe' and 'Modified Recipe'.",
            "The recipe should include all the given ingredients.",
            "The modified recipe should adhere to the specified dietary restriction.",
            "The recipe should be clear, detailed, and include all necessary steps and measurements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
