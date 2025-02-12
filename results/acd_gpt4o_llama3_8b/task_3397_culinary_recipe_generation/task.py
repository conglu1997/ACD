class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Create a dessert recipe that includes chocolate, berries, and a crunchy element. The recipe should be suitable for a special occasion and should serve at least four people.",
                "instructions": "Generate a detailed recipe for a dessert based on the given criteria. Ensure the recipe includes an ingredient list, step-by-step instructions, and any special tips or tricks. The recipe should be suitable for a special occasion and serve at least four people. Submit your response as a plain text string in the following format: \nRecipe Name: [Your recipe name] \nIngredients: [List of ingredients] \nInstructions: [Step-by-step instructions] \nTips: [Any special tips or tricks]"
            },
            "2": {
                "data": "Interpret the following recipe and explain the steps and rationale behind it: \nRecipe Name: Spaghetti Carbonara \nIngredients: \n- 200g spaghetti \n- 100g pancetta \n- 2 large eggs \n- 50g pecorino cheese \n- 50g parmesan \n- 2 cloves of garlic \n- Freshly ground black pepper \n- Salt \n \nInstructions: \n1. Cook the spaghetti in a large pot of boiling salted water until al dente. \n2. Meanwhile, beat the eggs in a bowl, then grate and mix in the cheeses. \n3. Fry the pancetta with the garlic until crispy. Remove the garlic. \n4. Drain the spaghetti and add it to the pancetta. Remove from heat. \n5. Quickly pour in the egg and cheese mixture, stirring vigorously to create a creamy sauce. \n6. Season with salt and plenty of black pepper. Serve immediately.",
                "instructions": "Interpret the given recipe and explain the steps and rationale behind it. Include details about the purpose of each step, the role of key ingredients, and any important techniques used. Submit your response as a plain text string in the following format: \nInterpretation: [Your interpretation] \nRationale: [Explanation of steps and techniques]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['instructions']}\n\nHere is the data for the task:\n\n{t['data']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'Chocolate Dessert' in t['data']:
            validation_criteria = [
                "The recipe should include chocolate, berries, and a crunchy element.",
                "The recipe should be suitable for a special occasion and serve at least four people.",
                "The recipe should be detailed and plausible, including all necessary steps."
            ]
        else:
            validation_criteria = [
                "The interpretation should accurately explain the steps and rationale behind the recipe.",
                "The explanation should include details about the purpose of each step, the role of key ingredients, and any important techniques used.",
                "The explanation should be coherent and logically organized."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
