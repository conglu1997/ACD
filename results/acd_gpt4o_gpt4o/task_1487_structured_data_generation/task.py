class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": {"name": "Jane Smith", "age": 28, "address": {"street": "456 Elm St", "city": "Othertown", "zipcode": "67890"}, "contacts": [{"type": "email", "value": "jane.smith@example.com"}, {"type": "phone", "value": "555-6789"}], "employment": {"status": "employed", "position": "Software Engineer", "company": "TechCorp", "start_date": "2020-01-15"}}},
            "2": {"json_data": {"order_id": "12345", "customer": {"name": "Alice Johnson", "email": "alice.johnson@example.com", "phone": "555-9876"}, "items": [{"product": "Smartphone", "quantity": 1, "price": 699.99}, {"product": "Wireless Charger", "quantity": 2, "price": 29.99}], "total": 759.97, "status": "Shipped"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "criteria" in t:
            criteria = t["criteria"]
            instructions = f"""Your task is to generate a JSON structure based on the following criteria:\n\n{criteria}\n\nEnsure that the JSON structure is correctly formatted and accurately represents the provided criteria. Provide your response in plain text format."""
        else:
            json_data = t["json_data"]
            instructions = f"""Your task is to interpret the following JSON structure and describe its contents in plain text:\n\n{json_data}\n\nEnsure that your description is accurate and covers all the elements of the JSON structure. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "criteria" in t:
            criteria.append("The JSON structure should be correctly formatted.")
            criteria.append("The JSON structure should accurately represent the provided criteria.")
        else:
            criteria.append("The description should accurately cover all elements of the JSON structure.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
