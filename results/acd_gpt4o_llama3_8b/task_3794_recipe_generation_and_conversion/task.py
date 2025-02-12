class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Convert the following list of ingredients into a detailed recipe: 3 cups of all-purpose flour, 1 and 1/2 cups of granulated sugar, 1 cup of unsalted butter (softened), 4 large eggs, 2 teaspoons of vanilla extract, 1 and 1/2 teaspoons of baking powder, 1/2 teaspoon of baking soda, 1/2 teaspoon of salt, 1 cup of whole milk, 1/2 cup of sour cream.",
                "constraints": "The recipe should include clear and logical steps for combining and cooking the ingredients to create a cake. Ensure the recipe covers all steps, including preparation, mixing, baking, and cooling. Do not omit any ingredients or steps."
            },
            "2": {
                "description": "Convert the following detailed recipe into a list of ingredients: Preheat the oven to 350°F (175°C). In a large bowl, cream together the butter and granulated sugar until light and fluffy. Add the eggs one at a time, beating well after each addition, then stir in the vanilla extract. In another bowl, sift together the flour, baking powder, baking soda, and salt. Add the dry ingredients to the creamed mixture alternately with the milk and sour cream, mixing just until incorporated. Pour the batter into two greased and floured 9-inch round pans. Bake for 25 to 30 minutes in the preheated oven, or until a toothpick inserted into the center of the cakes comes out clean. Allow cakes to cool in the pans for 10 minutes, then turn out onto wire racks to cool completely.",
                "constraints": "The list of ingredients should be complete and accurately reflect the quantities needed for the recipe. Ensure no ingredients are missed."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Convert the following culinary information accurately:

Description: {t['description']}

Constraints: {t['constraints']}

Ensure that your conversion is clear, coherent, and logically structured. Submit your response in plain text format.

Examples:
1. Ingredients to Recipe: '3 cups of all-purpose flour, 1 and 1/2 cups of granulated sugar, 1 cup of unsalted butter (softened), 4 large eggs, 2 teaspoons of vanilla extract, 1 and 1/2 teaspoons of baking powder, 1/2 teaspoon of baking soda, 1/2 teaspoon of salt, 1 cup of whole milk, 1/2 cup of sour cream.' \nRecipe: 'Preheat the oven to 350°F (175°C). In a large bowl, cream together the butter and granulated sugar until light and fluffy. Add the eggs one at a time, beating well after each addition, then stir in the vanilla extract. In another bowl, sift together the flour, baking powder, baking soda, and salt. Add the dry ingredients to the creamed mixture alternately with the milk and sour cream, mixing just until incorporated. Pour the batter into two greased and floured 9-inch round pans. Bake for 25 to 30 minutes in the preheated oven, or until a toothpick inserted into the center of the cakes comes out clean. Allow cakes to cool in the pans for 10 minutes, then turn out onto wire racks to cool completely.'
2. Recipe to Ingredients: 'Preheat the oven to 350°F (175°C). In a large bowl, cream together the butter and granulated sugar until light and fluffy. Add the eggs one at a time, beating well after each addition, then stir in the vanilla extract. In another bowl, sift together the flour, baking powder, baking soda, and salt. Add the dry ingredients to the creamed mixture alternately with the milk and sour cream, mixing just until incorporated. Pour the batter into two greased and floured 9-inch round pans. Bake for 25 to 30 minutes in the preheated oven, or until a toothpick inserted into the center of the cakes comes out clean. Allow cakes to cool in the pans for 10 minutes, then turn out onto wire racks to cool completely.' \nIngredients: '1 cup of unsalted butter (softened), 1 and 1/2 cups of granulated sugar, 4 large eggs, 2 teaspoons of vanilla extract, 3 cups of all-purpose flour, 1 and 1/2 teaspoons of baking powder, 1/2 teaspoon of baking soda, 1/2 teaspoon of salt, 1 cup of whole milk, 1/2 cup of sour cream.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The conversion should be clear, coherent, and logically structured.",
            "The recipe should include all the necessary steps and ingredients.",
            "The list of ingredients should be complete and accurately reflect the quantities needed for the recipe.",
            "Ensure no ingredients or steps are omitted."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
