class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate", "format": "JSON", "specification": {"name": "string", "age": "integer", "address": {"street": "string", "city": "string", "postcode": "string"}}},
            "2": {"type": "interpret", "format": "XML", "data": "<person><name>John Doe</name><age>30</age><address><street>Main St</street><city>Metropolis</city><postcode>12345</postcode></address></person>", "query": "Extract the city and postcode."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate":
            format = t["format"]
            specification = t["specification"]
            instructions = f"""Your task is to generate {format} data based on the given specification.

Specification: {specification}

Ensure the generated data is valid {format} and adheres to the specification. Provide the {format} data in plain text format. Example of valid JSON:
{{"name": "John Doe", "age": 30, "address": {{"street": "Main St", "city": "Metropolis", "postcode": "12345"}}}}"""
        elif t["type"] == "interpret":
            format = t["format"]
            data = t["data"]
            query = t["query"]
            instructions = f"""Your task is to interpret the given {format} data and extract information based on the specified query.

Data: {data}
Query: {query}

Provide your response in plain text format, ensuring the extracted information is accurate and complete. Example response format:
City: Metropolis, Postcode: 12345"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate":
            criteria = [
                "The generated data should be valid {t['format']}.",
                "The data should adhere to the given specification.",
                "The structure of the data should match the example format provided in the instructions."
            ]
        elif t["type"] == "interpret":
            criteria = [
                "The extracted information should be accurate.",
                "The response should be complete and relevant to the query.",
                "The format of the response should match the example provided in the instructions."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
