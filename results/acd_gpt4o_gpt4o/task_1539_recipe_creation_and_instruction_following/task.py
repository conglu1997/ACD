class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a vegetarian pasta recipe that includes at least one type of vegetable, one type of cheese, and a homemade sauce. Ensure the recipe serves four people.", "task_type": "creation"},
            "2": {"instructions": "1. Preheat the oven to 180°C (350°F). 2. Mix 2 cups of flour, 1 cup of sugar, and 1 teaspoon of baking powder. 3. Add 2 eggs and 1 cup of milk, then mix until smooth. 4. Pour the mixture into a greased baking dish. 5. Sprinkle 1/2 cup of chopped nuts on top. 6. Bake for 25-30 minutes or until a toothpick inserted into the center comes out clean. 7. Let it cool for 10 minutes before serving.", "task_type": "following"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "creation":
            return """Your task is to create a detailed recipe based on the following criteria:

{0}

Ensure that your recipe includes a list of ingredients with measurements, step-by-step cooking instructions, serving size, and any necessary tips for preparation. Provide your response in plain text format. Format your response as follows:

1. Ingredients: [List of ingredients with measurements]
2. Instructions: [Step-by-step cooking instructions]
3. Serving Size: [Number of servings]""".format(t["criteria"])
        elif t["task_type"] == "following":
            return """Your task is to follow the given step-by-step cooking instructions and provide a detailed description of the final dish. Ensure that your description includes the appearance, texture, and taste of the dish. Provide your response in plain text format. Format your response as follows:

1. Appearance: [Detailed description of the dish's appearance]
2. Texture: [Detailed description of the dish's texture]
3. Taste: [Detailed description of the dish's taste]""".format(t["instructions"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should be detailed, including a list of ingredients with measurements, step-by-step cooking instructions, serving size, and clear preparation tips." if t["task_type"] == "creation" else "The description of the final dish should accurately reflect the given cooking instructions, including appearance, texture, and taste."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
