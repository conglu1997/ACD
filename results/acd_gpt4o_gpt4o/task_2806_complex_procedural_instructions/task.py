class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "instructions": [
                    "1. Preheat the oven to 350 degrees Fahrenheit.",
                    "2. In a bowl, mix 2 cups of flour, 1 cup of sugar, and 1 teaspoon of baking powder.",
                    "3. In another bowl, whisk together 2 eggs, 1 cup of milk, and 1/2 cup of melted butter.",
                    "4. Combine the wet and dry ingredients, stirring until smooth.",
                    "5. Pour the batter into a greased baking pan.",
                    "6. Bake for 30 minutes or until a toothpick inserted into the center comes out clean.",
                    "7. Let the cake cool before serving.",
                    "8. Optional: Frost the cake with your favorite icing after it has cooled.",
                    "9. Optional: Add sprinkles or other decorations if desired."
                ],
                "goal": "Describe the result of following the instructions and any potential issues that may arise if steps are not followed correctly."
            },
            "2": {
                "instructions": [
                    "1. Gather the following materials: cardboard, scissors, glue, colored paper, and a ruler.",
                    "2. Cut the cardboard into a rectangular shape, 12 inches by 8 inches.",
                    "3. Cover the cardboard with colored paper using glue.",
                    "4. Measure and cut out shapes (like stars, circles) from additional colored paper.",
                    "5. Glue the paper shapes onto the covered cardboard in a decorative pattern.",
                    "6. Let the glue dry for at least 1 hour.",
                    "7. Optional: Add additional decorations like stickers or glitter if desired.",
                    "8. Optional: Frame the decorated cardboard for display."
                ],
                "goal": "Describe the result of following the instructions and any potential issues that may arise if steps are not followed correctly."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to follow the series of complex procedural instructions provided below to achieve a specified outcome. After carefully reading and mentally following the instructions, describe the final result and any potential issues that may arise if the steps are not followed correctly.

Instructions: {' '.join(t['instructions'])}

Your description should be clear, detailed, and between 150 and 300 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be clear and detailed.",
            "The explanation should identify potential issues if steps are not followed correctly.",
            "The response should be between 150 and 300 words long.",
            "The response should demonstrate an understanding of the sequence and dependencies in the instructions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
