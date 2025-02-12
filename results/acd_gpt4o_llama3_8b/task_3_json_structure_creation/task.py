class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "specifications": "Create a JSON object representing a book with the following fields: title (string), author (string), year (integer), genres (array of strings), and reviews (array of objects with fields: reviewer (string) and rating (integer))."
            },
            "2": {
                "specifications": "Create a JSON object representing a company with the following fields: name (string), founded (integer), employees (array of objects with fields: name (string), position (string), and tenure (integer)), and locations (array of strings)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a nested JSON structure based on the given specifications: {t["specifications"]}. Ensure the JSON is properly formatted and includes all the required fields with appropriate data types. Here is an example of the expected JSON format:

Example for a book:
{{
  'title': 'Example Book',
  'author': 'Author Name',
  'year': 2021,
  'genres': ['Fiction', 'Adventure'],
  'reviews': [
    {{'reviewer': 'Reviewer1', 'rating': 5}},
    {{'reviewer': 'Reviewer2', 'rating': 4}}
  ]
}}

Example for a company:
{{
  'name': 'Example Company',
  'founded': 1999,
  'employees': [
    {{'name': 'Employee1', 'position': 'Manager', 'tenure': 5}},
    {{'name': 'Employee2', 'position': 'Developer', 'tenure': 3}}
  ],
  'locations': ['New York', 'San Francisco']
}}
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import json
        from src.eval_helper import eval_with_llm_judge
        try:
            parsed_submission = json.loads(submission)
        except json.JSONDecodeError:
            return 0.0

        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The JSON structure should match the given specifications.",
            "The data types of the fields should be correct.",
            "The JSON should be properly formatted."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
