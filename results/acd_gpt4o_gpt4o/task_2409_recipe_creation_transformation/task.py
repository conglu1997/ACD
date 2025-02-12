class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "original_recipe": "Spaghetti Carbonara",
                "constraints": ["Make it vegetarian", "Maintain a creamy texture", "Avoid using dairy products"]
            },
            "2": {
                "original_recipe": "Chicken Caesar Salad",
                "constraints": ["Make it vegan", "Include a source of plant-based protein", "Maintain a rich flavor", "Avoid using any animal products"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to transform the given recipe based on the specified constraints. "
            "Ensure that the transformed recipe maintains the original dish's essence while adhering to the constraints. "
            "Provide the transformed recipe in the following format: \n\n"
            "1. Title of the transformed recipe \n"
            "2. List of ingredients \n"
            "3. Step-by-step cooking instructions"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed recipe should adhere to the specified constraints.",
            "The new recipe should be coherent and followable.",
            "The transformed recipe should maintain the essence of the original dish.",
            "The recipe should be detailed and easy to follow.",
            "The recipe should avoid using any restricted ingredients as per the constraints."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
