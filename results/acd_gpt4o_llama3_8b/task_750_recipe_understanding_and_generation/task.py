class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "recipe": "Ingredients:\n- 2 cups flour\n- 1 cup sugar\n- 1/2 cup butter\n- 2 eggs\n- 1 tsp vanilla extract\n- 1 tsp baking powder\n- 1/2 tsp salt\n- 1 cup milk\n\nInstructions:\n1. Preheat the oven to 350°F (175°C).\n2. In a bowl, cream together the butter and sugar until light and fluffy.\n3. Beat in the eggs one at a time, then stir in the vanilla extract.\n4. Combine the flour, baking powder, and salt; gradually add to the creamed mixture alternately with the milk.\n5. Pour batter into a greased 9x9 inch pan.\n6. Bake for 30 to 35 minutes in the preheated oven, until a toothpick inserted into the center of the cake comes out clean.\n7. Let cool in the pan for 10 minutes, then turn out onto a wire rack to cool completely.",
                "criteria": "Create a new recipe for a chocolate cake that serves 8 people. Include all necessary ingredients and detailed instructions."
            },
            "2": {
                "recipe": "Ingredients:\n- 1 cup quinoa\n- 2 cups water\n- 1/2 tsp salt\n- 1/4 cup olive oil\n- 1/2 cup chopped onion\n- 1/2 cup chopped bell pepper\n- 1/2 cup chopped zucchini\n- 1/2 cup chopped tomato\n- 1 tsp garlic powder\n- 1 tsp cumin\n- 1/2 tsp paprika\n- Salt and pepper to taste\n\nInstructions:\n1. Rinse the quinoa under cold water.\n2. In a medium saucepan, bring the water and salt to a boil.\n3. Add the quinoa, reduce the heat to low, cover, and simmer for 15 minutes or until all the water is absorbed.\n4. In a large skillet, heat the olive oil over medium heat.\n5. Add the onion, bell pepper, zucchini, and tomato; sauté until tender.\n6. Stir in the cooked quinoa, garlic powder, cumin, and paprika.\n7. Season with salt and pepper to taste.\n8. Cook for an additional 5 minutes, stirring occasionally.\n9. Serve warm.",
                "criteria": "Create a new recipe for a healthy salad that includes at least three different vegetables and a homemade dressing. Include all necessary ingredients and detailed instructions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a recipe to understand and summarize, followed by a task to generate a new recipe based on specific criteria.\n\nRecipe:\n{t['recipe']}\n\nTask:\n{t['criteria']}\n\nYour response should include:\n1. A brief summary of the given recipe.\n2. A new recipe based on the provided criteria, including all necessary ingredients and detailed instructions.\n\nSubmit your response as a plain text string with clearly labeled sections for 'Summary' and 'New Recipe'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a brief summary of the given recipe.",
            "The response should include a new recipe based on the provided criteria, including all necessary ingredients and detailed instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
