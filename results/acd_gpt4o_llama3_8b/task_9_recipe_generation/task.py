class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "specifications": "Create a recipe for a vegan chocolate cake. The recipe should include the following sections: Ingredients, Instructions, and Notes. The Instructions section should contain at least 5 steps."
            },
            "2": {
                "specifications": "Create a recipe for a classic margherita pizza. The recipe should include the following sections: Ingredients, Instructions, and Notes. The Instructions section should contain at least 5 steps."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a recipe based on the given specifications: {t["specifications"]}. Ensure the recipe is properly formatted and includes all the required sections. Here is an example of the expected format:

Example for a recipe:

Ingredients:
- 2 cups flour
- 1 cup sugar
- 1/2 cup cocoa powder
- 1 tsp baking powder
- 1/2 tsp salt

Instructions:
1. Preheat the oven to 350°F (175°C).
2. In a large bowl, mix the dry ingredients together.
3. Add wet ingredients and mix until smooth.
4. Pour the batter into a greased baking pan.
5. Bake for 30-35 minutes or until a toothpick inserted into the center comes out clean.

Notes:
- You can add nuts or chocolate chips for extra texture.
- Store the cake in an airtight container to keep it fresh.

Ensure that the "Ingredients", "Instructions", and "Notes" sections are clearly separated and well-formatted. The "Instructions" section should contain sequential steps that are easy to follow."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The recipe should include the Ingredients, Instructions, and Notes sections.",
            "The Instructions section should contain at least 5 steps.",
            "The recipe should be properly formatted and coherent.",
            "The Instructions should be sequential and clear."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
