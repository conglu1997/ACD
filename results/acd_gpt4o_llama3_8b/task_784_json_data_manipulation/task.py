class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a JSON structure representing a list of employees with their details and then query the structure to find employees in a particular department.",
                "requirements": {
                    "departments": ["HR", "Engineering", "Marketing"],
                    "fields": ["name", "age", "department"]
                },
                "query": "Find all employees in the Engineering department."
            },
            "2": {
                "description": "Generate a JSON structure representing a library's collection of books and then query the structure to find books by a particular author.",
                "requirements": {
                    "fields": ["title", "author", "year", "genre"]
                },
                "query": "Find all books written by 'J.K. Rowling'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a JSON structure based on the following requirements and then perform the specified query on the structure.

Requirements: {t['requirements']}
Query: {t['query']}

Ensure your JSON structure is valid and correctly formatted. Submit your response as a plain text string in the following format:

JSON Structure:
[Your JSON structure here]

Query Result:
[Your query result here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The JSON structure should be valid and correctly formatted.",
            "The JSON structure should contain the required fields.",
            "The query result should be correct based on the provided JSON structure and query."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
