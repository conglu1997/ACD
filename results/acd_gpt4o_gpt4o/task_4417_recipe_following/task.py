class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ingredients": ["chicken breast", "olive oil", "garlic", "lemon", "rosemary", "salt", "pepper", "white wine"],
                "instructions": "Generate a detailed cooking recipe using the given ingredients. Predict the taste, texture, and aroma of the final dish." 
            },
            "2": {
                "ingredients": ["flour", "sugar", "butter", "eggs", "vanilla extract", "baking powder", "milk", "cocoa powder"],
                "instructions": "Generate a detailed cooking recipe using the given ingredients. Predict the appearance, flavor, and texture of the final dish."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ingredients = ", ".join(t["ingredients"])
        instructions = t["instructions"]
        return f"""Your task is to generate a detailed cooking recipe using the given ingredients.

Ingredients:
{ingredients}

{instructions}

Provide your response in plain text format. Your response should include:
1. A step-by-step recipe.
2. A prediction of the outcome (e.g., taste, texture, aroma, appearance, or flavor).
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a coherent and logical step-by-step recipe.",
            "The response should use all the given ingredients appropriately.",
            "The response should include a prediction of the outcome (taste, texture, aroma, appearance, or flavor)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
