class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "creation",
                "constraints": "Create a vegan dessert recipe that includes chocolate and coconut as primary ingredients. The recipe should be easy to follow and contain a list of ingredients and step-by-step instructions."
            },
            "2": {
                "task_type": "analysis",
                "recipe": "Ingredients: 1 cup flour, 1/2 cup sugar, 1/2 cup butter, 2 eggs, 1 tsp vanilla extract, 1/2 cup milk. Instructions: Mix all ingredients and bake at 350°F for 30 minutes.",
                "dietary_restriction": "gluten-free"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'creation':
            return f"""Your task is to create a vegan dessert recipe based on the following constraints:

Constraints: {t['constraints']}

Ensure your recipe includes a list of ingredients and detailed step-by-step instructions. The recipe should be easy to follow and suitable for a vegan diet. Provide your response in plain text format.

Expected format:
Ingredients: [List of ingredients]
Instructions: [Step-by-step instructions]
Example:
Ingredients: 
- 1 cup flour
- 1/2 cup cocoa powder
- 1 cup coconut milk
- 1/2 cup maple syrup
- 1/4 cup shredded coconut
- 1/2 cup vegan chocolate chips

Instructions:
1. Preheat the oven to 350°F (175°C).
2. In a bowl, mix flour, cocoa powder, and shredded coconut.
3. Add coconut milk and maple syrup, and stir until smooth.
4. Fold in the vegan chocolate chips.
5. Pour the mixture into a baking dish and bake for 25 minutes.
6. Allow to cool before serving.
"""
        elif t['task_type'] == 'analysis':
            return f"""Your task is to analyze the following recipe and determine if it is suitable for someone following a {t['dietary_restriction']} diet:

Recipe: {t['recipe']}

Provide a clear analysis explaining whether the recipe meets the dietary restriction and suggest any necessary modifications to make it compliant. Identify any ingredients that do not meet the dietary restriction. Provide your response in plain text format.

Expected format:
Analysis: [Your analysis]
Modifications: [Suggested modifications, if any]
Example:
Analysis: The recipe is not suitable for a gluten-free diet because it contains flour, which typically contains gluten. Additionally, the recipe contains butter, which is not suitable for a dairy-free diet.
Modifications: Substitute the flour with a gluten-free flour blend. Replace the butter with a dairy-free alternative such as vegan margarine or coconut oil.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'creation':
            criteria = [
                "The recipe includes a list of ingredients.",
                "The recipe includes detailed step-by-step instructions.",
                "The recipe is suitable for a vegan diet.",
                "The recipe prominently features chocolate and coconut as primary ingredients."
            ]
        elif t['task_type'] == 'analysis':
            criteria = [
                "The analysis correctly identifies whether the recipe meets the dietary restriction.",
                "The analysis identifies any ingredients that do not meet the dietary restriction.",
                "The analysis provides clear reasoning for the determination.",
                "If necessary, the modifications suggested are appropriate and make the recipe compliant with the dietary restriction."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
