class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"recipe": "To make a simple chocolate cake, you will need the following ingredients: 1 cup of sugar, 1/2 cup of butter, 2 eggs, 1 teaspoon of vanilla extract, 1 and 1/2 cups of flour, 1 and 3/4 teaspoons of baking powder, and 1/2 cup of milk. First, preheat your oven to 350 degrees F (175 degrees C). In a medium bowl, cream together the sugar and butter. Beat in the eggs, one at a time, then stir in the vanilla. Combine flour and baking powder, add to the creamed mixture and mix well. Finally, stir in the milk until the batter is smooth. Pour or spoon batter into the prepared pan. Bake for 30 to 40 minutes in the preheated oven. The cake is done when it springs back to the touch. Let cool before serving.", "missing": "ingredient", "index": 2, "hints": "Consider the role of each ingredient in baking a cake."},
            "2": {"recipe": "To prepare a classic Caesar salad, you will need the following ingredients: 1 head of romaine lettuce, 1/2 cup of grated Parmesan cheese, 1 cup of croutons, 1/2 cup of Caesar dressing. First, wash and chop the romaine lettuce. In a large bowl, combine the lettuce and Parmesan cheese. Add the croutons and toss the salad gently. Next, drizzle the Caesar dressing over the salad and toss until everything is evenly coated. Serve immediately.", "missing": "step", "index": 4, "hints": "Think about the sequence of steps in preparing a salad."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["missing"] == "ingredient":
            return f"""Your task is to identify the missing ingredient in the following recipe: {t["recipe"]}. Provide the missing ingredient based on the context of the recipe. Format your response as follows: Missing Ingredient: [Your answer]"""
        else:
            return f"""Your task is to identify the missing step in the following recipe: {t["recipe"]}. Provide the missing step based on the context of the recipe. Format your response as follows: Missing Step: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["missing"] == "ingredient":
            criteria = ["The response should correctly identify the missing ingredient based on the recipe context."]
        else:
            criteria = ["The response should correctly identify the missing step based on the recipe context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
