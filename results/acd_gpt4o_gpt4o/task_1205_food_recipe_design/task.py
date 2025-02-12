class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Create a vegan dessert using only the following ingredients: coconut milk, maple syrup, almonds, and dark chocolate. The dessert should be gluten-free and low-calorie."
            },
            "2": {
                "criteria": "Design a gluten-free main course using chicken, quinoa, spinach, and bell peppers. Ensure the dish is high in protein and low in sodium."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        criteria = t["criteria"]
        instructions = f"""Your task is to design a novel food recipe based on the following criteria:

{criteria}

Your response should include:
1. The name of the dish.
2. A list of ingredients with measurements.
3. Step-by-step preparation instructions.
4. Detailed nutritional information, including calorie count, protein content, and sodium content.

Provide your response in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should adhere to the specified dietary requirements.",
            "The recipe should use only the given ingredients.",
            "The preparation instructions should be clear and easy to follow.",
            "The nutritional information should be detailed and accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
