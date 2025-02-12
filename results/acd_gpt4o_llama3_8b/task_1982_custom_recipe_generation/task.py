class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "vegan, gluten-free, high-protein",
                "ingredients": "quinoa, chickpeas, spinach, tomatoes",
                "cuisine": "Mediterranean"
            },
            "2": {
                "constraints": "keto, dairy-free",
                "ingredients": "cauliflower, chicken, avocado, lime",
                "cuisine": "Mexican"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a recipe based on the following constraints, ingredients, and cuisine type.

Constraints: {t['constraints']}
Ingredients: {t['ingredients']}
Cuisine: {t['cuisine']}

Your response should include:
1. The name of the dish.
2. A list of ingredients with quantities.
3. Step-by-step instructions for preparing the dish.
4. An optional note on the nutritional benefits of the dish.

Example response format:
- Dish Name: Vegan Quinoa Salad
- Ingredients:
  - 1 cup quinoa
  - 1 can chickpeas, drained and rinsed
  - 2 cups spinach, chopped
  - 1 cup cherry tomatoes, halved
  - 1/4 cup olive oil
  - 2 tbsp lemon juice
  - Salt and pepper to taste
- Instructions:
  1. Cook the quinoa according to package instructions and let it cool.
  2. In a large bowl, combine the quinoa, chickpeas, spinach, and cherry tomatoes.
  3. In a small bowl, whisk together the olive oil, lemon juice, salt, and pepper.
  4. Pour the dressing over the salad and toss to combine.
  5. Serve immediately or refrigerate for later.
- Note: This vegan quinoa salad is high in protein and rich in essential vitamins and minerals, making it a nutritious and satisfying meal.

Ensure your recipe is clear, well-structured, and adheres to the given constraints. Submit your response as a plain text string in the specified format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The recipe should adhere to the specified dietary constraints.",
            "The recipe should include all the given ingredients.",
            "The recipe should reflect the specified cuisine type.",
            "The recipe should be clear and well-structured.",
            "The recipe should be creative and plausible.",
            "The recipe should have a logical sequence of steps.",
            "The recipe should specify quantities for each ingredient.",
            "The optional nutritional note, if included, should be accurate and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
