class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate a detailed recipe for a vegan and gluten-free pasta dish that includes at least 5 ingredients and 3 cooking steps.",
                "interpret": "Pasta Primavera: Ingredients: 200g gluten-free pasta, 1 bell pepper, 1 zucchini, 1/2 cup cherry tomatoes, 2 tbsp olive oil, salt, pepper. Steps: 1. Cook pasta according to package instructions. 2. In a pan, heat olive oil and sauté bell pepper and zucchini until tender. 3. Add cherry tomatoes and cooked pasta to the pan, season with salt and pepper, and toss to combine."
            },
            "2": {
                "prompt": "Generate a detailed recipe for a chocolate cake that includes at least 6 ingredients and 4 cooking steps.",
                "interpret": "Chocolate Cake: Ingredients: 2 cups flour, 1 cup sugar, 1/2 cup cocoa powder, 1 tsp baking powder, 2 eggs, 1 cup milk, 1/2 cup melted butter, 1 tsp vanilla extract. Steps: 1. Preheat oven to 350°F (175°C). 2. In a bowl, mix together flour, sugar, cocoa powder, and baking powder. 3. Add eggs, milk, melted butter, and vanilla extract, and stir until well combined. 4. Pour the batter into a greased cake pan and bake for 30-35 minutes or until a toothpick inserted into the center comes out clean. 5. Allow the cake to cool before serving."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given two tasks. First, generate a detailed cooking recipe based on the given prompt. Second, interpret the provided recipe to extract the list of ingredients and the cooking steps.

Task 1: {t['prompt']}
Task 2: Interpret the following recipe:
{t['interpret']}

Submit your response in the following format:
Recipe: [Your generated recipe]
Ingredients: [Extracted list of ingredients]
Steps: [Extracted list of cooking steps]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated recipe should be detailed and include the specified dietary restrictions, number of ingredients, and cooking steps.",
            "The interpreted recipe should accurately extract the list of ingredients and cooking steps.",
            "The response should include both tasks in the correct format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
