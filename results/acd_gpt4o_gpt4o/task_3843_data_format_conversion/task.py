class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"csv_data": "name,age,city\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago\nDiana,40,San Francisco\nEvan,28,Houston"},
            "2": {"json_data": "[{\"name\": \"Alice\", \"age\": 30, \"city\": \"New York\"}, {\"name\": \"Bob\", \"age\": 25, \"city\": \"Los Angeles\"}, {\"name\": \"Charlie\", \"age\": 35, \"city\": \"Chicago\"}, {\"name\": \"Diana\", \"age\": 40, \"city\": \"San Francisco\"}, {\"name\": \"Evan\", \"age\": 28, \"city\": \"Houston\"}]"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "csv_data" in t:
            instructions = f"""Your task is to convert the following CSV data into a JSON array of objects:

{t['csv_data']}

Ensure that each row in the CSV is converted to a JSON object, with the column headers as keys. The output should be a JSON array containing these objects. Provide your response in plain text format as a single JSON array."""
        elif "json_data" in t:
            instructions = f"""Your task is to convert the following JSON array of objects into CSV format:

{t['json_data']}

Ensure that the CSV includes a header row with the keys from the JSON objects as column headers. Each subsequent row should contain the corresponding values. Provide your response in plain text format as a single CSV string."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "csv_data" in t:
            criteria = [
                "The JSON output should be a valid JSON array.",
                "Each CSV row should be correctly converted to a JSON object.",
                "The keys in the JSON objects should match the CSV headers."]
        elif "json_data" in t:
            criteria = [
                "The CSV output should be correctly formatted.",
                "The CSV should include a header row with keys from the JSON objects.",
                "Each JSON object should be correctly converted to a CSV row."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
