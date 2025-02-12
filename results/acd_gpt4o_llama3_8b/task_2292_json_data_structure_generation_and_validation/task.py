class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"specification": {"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "integer"}, "email": {"type": "string"}, "address": {"type": "object", "properties": {"street": {"type": "string"}, "city": {"type": "string"}, "zipcode": {"type": "string"}}}}}},
            "2": {"json_data": "{\"name\": \"John Doe\", \"age\": 30, \"email\": \"john.doe@example.com\", \"address\": {\"street\": \"123 Main St\", \"city\": \"Anytown\", \"zipcode\": \"12345\"}}"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        import json
        if "specification" in t:
            return f"""Generate a JSON data structure that adheres to the following specification:

{json.dumps(t['specification'], indent=2)}

Ensure that the JSON structure is valid and follows the given specification. Submit your response as a plain text string in JSON format."""
        elif "json_data" in t:
            return f"""Validate the following JSON data structure against the provided specification:

Specification: {json.dumps({"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "integer"}, "email": {"type": "string"}, "address": {"type": "object", "properties": {"street": {"type": "string"}, "city": {"type": "string"}, "zipcode": {"type": "string"}}}}}, indent=2)}

JSON Data: {t['json_data']}

Ensure that the JSON data is valid and follows the given specification. Submit your response as a plain text string indicating whether the JSON data is valid or not, along with any errors found."""
        else:
            raise ValueError("Invalid task format")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "specification" in t:
            criteria = ["The generated JSON structure should be valid.", "The JSON structure should adhere to the provided specification."]
        elif "json_data" in t:
            criteria = ["The validation result should be correct.", "Any errors found should be clearly identified."]
        else:
            raise ValueError("Invalid task format")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
