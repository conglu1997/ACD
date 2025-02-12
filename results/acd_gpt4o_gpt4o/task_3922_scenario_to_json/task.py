class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A university course with specific details", "requirements": {"course_name": {"type": "string"}, "instructor": {"type": "string"}, "credits": {"type": "integer"}, "schedule": {"type": "object", "properties": {"days": {"type": "array", "items": {"type": "string"}}, "time": {"type": "string"}}, "required": ["days", "time"]}}},
            "2": {"scenario": "A product in an e-commerce platform", "requirements": {"product_name": {"type": "string"}, "price": {"type": "number"}, "availability": {"type": "boolean"}, "categories": {"type": "array", "items": {"type": "string"}}}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to convert the following scenario description into a structured JSON object according to the specified requirements.

Scenario: {t['scenario']}

Requirements: {t['requirements']}

Ensure that the JSON object adheres to the specified structure and accurately represents the given scenario. Provide your response in JSON format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import json
        from jsonschema import validate, ValidationError
        from src.eval_helper import eval_with_llm_judge

        instructions = TaskFamily.get_instructions(t)

        try:
            submission_json = json.loads(submission)
        except json.JSONDecodeError:
            return 0.0

        schema = {"type": "object", "properties": t['requirements'], "required": list(t['requirements'].keys())}

        try:
            validate(instance=submission_json, schema=schema)
        except ValidationError:
            return 0.0

        criteria = [f"The JSON object should adhere to the specified structure and accurately represent the scenario: {t['scenario']}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
