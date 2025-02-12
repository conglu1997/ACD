class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "input_data": [
                    {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "hiking"]},
                    {"name": "Bob", "age": 25, "city": "San Francisco", "hobbies": ["gaming", "cooking"]},
                    {"name": "Charlie", "age": 35, "city": "Los Angeles", "hobbies": ["swimming", "cycling"]}
                ],
                "requirements": "Transform the given list of dictionaries into a dictionary where the keys are the city names and the values are lists of names of people living in those cities."
            },
            "2": {
                "input_data": [
                    {"product": "Laptop", "price": 1200, "quantity": 10},
                    {"product": "Smartphone", "price": 800, "quantity": 20},
                    {"product": "Tablet", "price": 600, "quantity": 15}
                ],
                "requirements": "Calculate the total inventory value for each product and return a dictionary where the keys are the product names and the values are the total inventory values. Total inventory value is calculated as price multiplied by quantity."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        import json
        return f"""Transform the given data structure based on the specified requirements: {t['requirements']} The input data is: {json.dumps(t['input_data'])}. Ensure the output is correctly formatted and meets the requirements. Submit your response as a JSON string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
