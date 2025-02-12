class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "nested_json": {
                    "user": {
                        "id": 1,
                        "name": "John Doe",
                        "contact": {
                            "email": "john.doe@example.com",
                            "phone": "123-456-7890"
                        },
                        "preferences": {
                            "notifications": {
                                "email": True,
                                "sms": False
                            },
                            "theme": "dark"
                        }
                    }
                },
                "instructions": "Change the user's theme to 'light' and set SMS notifications to True."
            },
            "2": {
                "nested_json": {
                    "order": {
                        "id": 102,
                        "date": "2023-10-01",
                        "customer": {
                            "name": "Alice Smith",
                            "address": {
                                "street": "123 Main St",
                                "city": "Anytown",
                                "zipcode": "12345"
                            }
                        },
                        "items": [
                            {
                                "id": 1,
                                "name": "Widget",
                                "quantity": 4,
                                "price": 19.99
                            },
                            {
                                "id": 2,
                                "name": "Gadget",
                                "quantity": 2,
                                "price": 29.99
                            }
                        ]
                    }
                },
                "instructions": "Add a new item to the order with id 3, name 'Thingamajig', quantity 1, and price 9.99."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        import json
        return f"""Your task is to manipulate the following nested JSON data according to the given instructions. Ensure that you follow the instructions accurately and maintain the structure of the JSON data.

JSON Data:
{json.dumps(t['nested_json'], indent=4)}

Instructions:
{t['instructions']}

Submit the modified JSON data in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The manipulated JSON data should accurately reflect the changes specified in the instructions.",
            "The structure of the JSON data should be maintained.",
            "The submission should be valid JSON."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
