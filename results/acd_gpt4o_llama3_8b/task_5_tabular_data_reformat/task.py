class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        task1 = {
            'data': 'Name, Age, City\nAlice, 30, New York\nBob, 25, Los Angeles\nCharles, 35, Chicago',
            'instructions': 'Convert the provided CSV data into a list of dictionaries, where each dictionary represents a row. The submission should be a JSON string in the following format: [{"Name": "Alice", "Age": 30, "City": "New York"}, {"Name": "Bob", "Age": 25, "City": "Los Angeles"}, {"Name": "Charles", "Age": 35, "City": "Chicago"}].'
        }
        task2 = {
            'data': 'Product, Price, Quantity\nLaptop, 1000, 5\nPhone, 500, 10\nTablet, 300, 7',
            'instructions': 'Convert the provided CSV data into a JSON object with an array of product details. The submission should be a JSON string in the following format: {"products": [{"Product": "Laptop", "Price": 1000, "Quantity": 5}, {"Product": "Phone", "Price": 500, "Quantity": 10}, {"Product": "Tablet", "Price": 300, "Quantity": 7}]}'
        }
        return {'1': task1, '2': task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""{t['instructions']}\n\nData:\n{t['data']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import json
        try:
            submission_data = json.loads(submission)
        except json.JSONDecodeError:
            return 0.0
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The submission should follow the exact JSON format specified in the instructions.',
            'The submission should accurately reflect the data provided.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0