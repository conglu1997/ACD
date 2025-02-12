class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "main_ingredient": "chicken breast",
                "dietary_restrictions": ["gluten-free", "dairy-free"],
                "expected_output": "A creative, nutritious, and flavorful recipe using chicken breast that is both gluten-free and dairy-free."
            },
            "2": {
                "main_ingredient": "tofu",
                "dietary_restrictions": ["vegan", "low-carb"],
                "expected_output": "A creative, nutritious, and flavorful recipe using tofu that is both vegan and low-carb."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        main_ingredient = t["main_ingredient"]
        dietary_restrictions = ", ".join(t["dietary_restrictions"])
        return f"""Create a recipe using the main ingredient '{main_ingredient}' that adheres to the following dietary restrictions: {dietary_restrictions}. Ensure the recipe is creative, nutritious, and flavorful. Include a list of ingredients, step-by-step instructions, and nutritional information. Submit your recipe as a plain text string in the following format:

Recipe Title: [Your recipe title]

Ingredients:
- [Ingredient 1]
- [Ingredient 2]
...

Instructions:
1. [Step 1]
2. [Step 2]
...

Nutritional Information:
- Calories: [Value]
- Protein: [Value]g
- Carbohydrates: [Value]g
- Fat: [Value]g
- Fiber: [Value]g

Example:

Recipe Title: Gluten-Free Dairy-Free Chicken Stir-Fry

Ingredients:
- 200g chicken breast
- 1 bell pepper
- 1 onion
- 2 cloves garlic
- 1 tbsp olive oil
- 100ml gluten-free soy sauce
- 50g cashews

Instructions:
1. Cut the chicken breast into strips.
2. Heat olive oil in a pan and sauté garlic and onion until translucent.
3. Add chicken strips and cook until browned.
4. Add bell pepper and cook for another 5 minutes.
5. Pour in gluten-free soy sauce and stir well.
6. Garnish with cashews and serve hot.

Nutritional Information:
- Calories: 350
- Protein: 30g
- Carbohydrates: 20g
- Fat: 15g
- Fiber: 5g"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe must use the main ingredient specified.", "The recipe must adhere to all listed dietary restrictions.", "The recipe must include ingredients, step-by-step instructions, and nutritional information.", "The recipe should be creative, nutritious, and flavorful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0