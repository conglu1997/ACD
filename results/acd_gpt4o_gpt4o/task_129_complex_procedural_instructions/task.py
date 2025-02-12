class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"procedure": [
                "Take a square piece of paper.",
                "Fold the paper in half diagonally to form a triangle.",
                "Fold the triangle in half again to form a smaller triangle.",
                "Fold the left corner of the triangle to the right corner.",
                "Cut a small triangle at the bottom tip.",
                "Unfold the paper to reveal a pattern."]},
            "2": {"procedure": [
                "Preheat the oven to 350 degrees Fahrenheit.",
                "Take a mixing bowl and add 1 cup of sugar, 1 cup of flour, and 1/2 cup of butter.",
                "Mix the ingredients thoroughly.",
                "Add 2 eggs and 1 teaspoon of vanilla extract to the mixture.",
                "Mix until the batter is smooth.",
                "Pour the batter into a greased baking dish.",
                "Bake for 30 minutes or until a toothpick inserted into the center comes out clean."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to follow the detailed instructions provided below and describe the final outcome:

{0}

Ensure that your description is accurate and reflects the result of following all the steps as given. Example response format: 'The final result is a piece of paper with a symmetrical pattern of cut-out shapes.'""".format('\n'.join(t["procedure"]))

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should accurately describe the outcome of following all the steps.",
            "The description should reflect the final result of the procedure clearly and correctly.",
            "The description should be detailed enough to understand the result without performing the steps." ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
