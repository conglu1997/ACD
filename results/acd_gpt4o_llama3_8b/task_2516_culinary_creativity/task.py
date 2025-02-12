class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ingredients": "chicken, garlic, lemon, thyme, olive oil, salt, pepper",
                "theme": "Mediterranean"
            },
            "2": {
                "ingredients": "salmon, soy sauce, ginger, honey, sesame seeds, green onions, rice",
                "theme": "Asian"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a recipe using the following ingredients and based on the given theme. Your recipe should include a title, a list of ingredients with realistic quantities, and step-by-step cooking instructions. Ensure that the recipe is creative, culturally authentic, and feasible to cook. Here are the details:

Ingredients: {t['ingredients']}
Theme: {t['theme']}

Submit your response as a plain text string in the following format:

Title: [Recipe title]

Ingredients:
- [Ingredient 1: Quantity]
- [Ingredient 2: Quantity]
...

Instructions:
1. [Step 1]
2. [Step 2]
...

Example:

Title: Mediterranean Lemon Chicken

Ingredients:
- Chicken: 4 pieces
- Garlic: 3 cloves, minced
- Lemon: 1, juiced
- Thyme: 2 tsp
- Olive oil: 2 tbsp
- Salt: to taste
- Pepper: to taste

Instructions:
1. Marinate the chicken in lemon juice, garlic, thyme, olive oil, salt, and pepper for 30 minutes.
2. Preheat the oven to 375°F (190°C).
3. Place the marinated chicken on a baking sheet and bake for 30-35 minutes or until fully cooked.
4. Serve hot with a side of vegetables or salad."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The recipe should include a title, a list of ingredients with realistic quantities, and step-by-step cooking instructions.",
            "The recipe should be creative and culturally authentic.",
            "The recipe should be feasible to cook."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
