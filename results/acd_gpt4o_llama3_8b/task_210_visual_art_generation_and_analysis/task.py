class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate an ASCII art of a tree with a simple structure (trunk and branches). Ensure the tree is symmetrical and spans at least 5 lines.",
                "example_output": "  ^  \n /|\n/ | \n  |  \n  |  "
            },
            "2": {
                "description": "Analyze the following ASCII art by providing a detailed textual description of what it depicts. Focus on the key elements, structure, and any notable features. ASCII Art:\n  /\\\n /  \\\n/____\\\n|    |\n|____|\n",
                "example_output": "The ASCII art depicts a simple house structure. The roof is triangular with two slanting lines forming the sides and one horizontal line at the base. The base of the house is rectangular with two vertical lines forming the sides and one horizontal line at the top and bottom."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task:

Description:
{t['description']}

Ensure your response meets the specified requirements. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = []
        if t['description'].startswith("Generate an ASCII art"):
            validation_criteria = ["The ASCII art should match the given description.", "The art should be symmetrical and span at least 5 lines if specified.", "The ASCII art should have a recognizable tree structure with a trunk and branches."]
        elif t['description'].startswith("Analyze the following ASCII art"):
            validation_criteria = ["The description should accurately reflect the ASCII art.", "The response should be detailed and cover key elements and notable features.", "The description should be at least 50 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
