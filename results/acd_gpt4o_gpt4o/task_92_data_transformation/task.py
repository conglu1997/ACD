class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"input_format": "json", "output_format": "xml", "data": {"person": {"name": "John Doe", "age": 30, "address": {"city": "New York", "zipcode": "10001"}}}},
            "2": {"input_format": "xml", "output_format": "json", "data": "<person><name>Jane Doe</name><age>25</age><address><city>Los Angeles</city><zipcode>90001</zipcode></address></person>"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        input_format = t["input_format"]
        output_format = t["output_format"]
        data = t["data"]
        instructions = f"""Your task is to convert the following data from {input_format} format to {output_format} format:

Data: {data}

Ensure that the converted data accurately represents the original data structure and content. Provide your response in plain text format with appropriate indentation and structure for the output format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The converted data should accurately represent the original data structure and content.", "The output should be well-formatted and properly indented for the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
