class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "Name, Age, Occupation\nJohn Doe, 28, Engineer\nJane Smith, 34, Doctor\nEmily Davis, 22, Student\nMichael Brown, 45, Pilot", "query": "Find the occupation of Michael Brown."},
            "2": {"data": "Product, Price, Quantity\nLaptop, 999.99, 10\nSmartphone, 499.99, 20\nTablet, 299.99, 15\nSmartwatch, 199.99, 25", "query": "Find the quantity of Smartwatch."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a structured data input in a CSV-like format. Your task is to extract specific information based on the given query. The data and query are provided below:

Data:
{t['data']}

Query:
{t['query']}

Your response should include only the extracted information in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include only the extracted information.",
            "The extracted information should be accurate based on the data provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
