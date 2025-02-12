class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"recipe_text": "Ingredients:\n- 2 cups of flour\n- 1 cup of sugar\n- 1/2 cup of butter\n- 2 eggs\n- 1 tsp of vanilla extract\n- 1/2 tsp of baking powder\n- 1/4 tsp of salt\n\nInstructions:\n1. Preheat the oven to 350°F (175°C).\n2. In a bowl, mix the flour, baking powder, and salt.\n3. In another bowl, beat the butter and sugar until creamy.\n4. Add the eggs and vanilla extract to the butter mixture and beat well.\n5. Gradually add the dry ingredients to the wet mixture, mixing until combined.\n6. Pour the batter into a greased baking pan.\n7. Bake for 25-30 minutes or until a toothpick inserted into the center comes out clean.\n8. Let the cake cool before serving."},
            "2": {"structured_format": {"ingredients": ["2 cups of flour", "1 cup of sugar", "1/2 cup of butter", "2 eggs", "1 tsp of vanilla extract", "1/2 tsp of baking powder", "1/4 tsp of salt"], "instructions": ["Preheat the oven to 350°F (175°C).", "In a bowl, mix the flour, baking powder, and salt.", "In another bowl, beat the butter and sugar until creamy.", "Add the eggs and vanilla extract to the butter mixture and beat well.", "Gradually add the dry ingredients to the wet mixture, mixing until combined.", "Pour the batter into a greased baking pan.", "Bake for 25-30 minutes or until a toothpick inserted into the center comes out clean.", "Let the cake cool before serving."]}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "recipe_text" in t:
            return f"""Convert the following detailed recipe text into a structured format with two sections: ingredients and instructions.\n\n{t["recipe_text"]}\n\nSubmit your response in the following format:\nIngredients: [List of ingredients]\nInstructions: [List of instructions]"""
        else:
            return f"""Generate a detailed recipe text from the following structured format:\n\nIngredients: {', '.join(t["structured_format"]["ingredients"])}\nInstructions: {', '.join(t["structured_format"]["instructions"])}\n\nSubmit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should accurately convert the recipe text into a structured format with correct ingredients and instructions." if "recipe_text" in t else "The response should accurately generate a detailed recipe text from the given structured format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
