class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A company has the following employees: John Doe, Senior Developer, 5 years experience; Jane Smith, Junior Developer, 2 years experience; Bob Johnson, Project Manager, 10 years experience. Create a structured JSON object representing this information.",
                "instruction": "Generate a structured JSON object based on the given employee information. Ensure the JSON object includes each employee's name, position, and years of experience. Submit your JSON object as a plain text string."
            },
            "2": {
                "description": "The following JSON object represents a list of products: {\"products\":[{\"name\":\"Laptop\",\"price\":1200,\"stock\":30,\"category\":\"electronics\"},{\"name\":\"Phone\",\"price\":600,\"stock\":50,\"category\":\"electronics\"},{\"name\":\"Tablet\",\"price\":300,\"stock\":20,\"category\":\"electronics\"},{\"name\":\"Chair\",\"price\":100,\"stock\":25,\"category\":\"furniture\"}]}. Extract and return the names of electronics products that have a stock greater than 20.",
                "instruction": "Extract the names of electronics products from the given JSON object that have a stock greater than 20. Submit your answer as a comma-separated string of product names."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"{t['instruction']} Description: {t['description']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'description' in t and 'Create a structured JSON object' in t['description']:
            criteria = [
                "The JSON object should include each employee's name, position, and years of experience.",
                "The JSON object should be well-structured and valid."
            ]
        else:
            criteria = [
                "The submission should list the names of electronics products with stock greater than 20.",
                "The names should be correctly extracted and formatted as a comma-separated string."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
