class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a table with 5 rows and 3 columns. The columns should be 'Name', 'Age', and 'Occupation'. Ensure the data is realistic and varied."
            },
            "2": {
                "description": "Create a table with 4 rows and 4 columns. The columns should be 'Product ID', 'Product Name', 'Price', and 'Stock Quantity'. Ensure the data is consistent and plausible."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate structured tabular data based on the following description:

Description: {t['description']}

Ensure the data is realistic, consistent, and follows the specified structure. Submit your table as a plain text string in the following format:

Column1 \t Column2 \t Column3 \t ...
Row1Value1 \t Row1Value2 \t Row1Value3 \t ...
Row2Value1 \t Row2Value2 \t Row2Value3 \t ...
...

Example:
Name \t Age \t Occupation
John Doe \t 30 \t Engineer
Jane Smith \t 25 \t Artist
Michael Brown \t 40 \t Teacher
Sarah White \t 35 \t Doctor
Anna Black \t 29 \t Writer

Product ID \t Product Name \t Price \t Stock Quantity
101 \t Widget A \t 19.99 \t 150
102 \t Widget B \t 29.99 \t 75
103 \t Widget C \t 9.99 \t 200
104 \t Widget D \t 49.99 \t 20
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The table should have the correct number of rows and columns.",
            "The data should be realistic and consistent.",
            "The table should follow the specified structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
