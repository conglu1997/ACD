class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_description": "Create a detailed recipe for making a chocolate cake. Include all necessary ingredients, steps, and tips for success. Additionally, ensure to mention the specific quantities required for each ingredient, and the exact temperature and time for baking. Format your response as follows: \n'Instructions: [Your detailed instructions]'"
            },
            "2": {
                "instructions": "1. Gather all necessary ingredients. 2. Preheat the oven to 350 degrees Fahrenheit. 3. Mix 2 cups of flour, 1 cup of sugar, and 1/2 cup of cocoa powder in a bowl. 4. Add 1 cup of milk, 2 eggs, and 1/2 cup of melted butter to the dry ingredients and stir until combined. 5. Pour the batter into a greased baking pan. 6. Bake for 25 minutes or until a toothpick inserted into the center comes out clean. 7. Let the cake cool for 10 minutes before removing it from the pan. 8. Frost with chocolate icing and serve.",
                "task_description": "Identify any potential errors or ambiguities in the provided instructions for making a cake. Provide a revised version with corrections and clarifications. Format your response as follows: \n'Errors/Ambiguities: [List of identified issues] \nRevised Instructions: [Your revised detailed instructions]'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'task_description' in t:
            return f"""{t['task_description']}"""
        else:
            return f"""{t['task_description']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'task_description' in t:
            validation_criteria = ["The instructions should be clear, logical, and complete.", "The instructions should include all necessary steps and details."]
        else:
            validation_criteria = ["Identified errors or ambiguities should be accurate.", "Revised instructions should be clear, logical, and complete.", "Revised instructions should correct all identified issues."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
