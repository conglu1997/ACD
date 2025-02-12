class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "software_spec": "A RESTful API for a to-do list application. The API should support the following operations: create a new to-do item, retrieve all to-do items, update a to-do item, and delete a to-do item. Each to-do item should have an ID, title, description, and status (completed or not completed)."
            },
            "2": {
                "software_spec": "A command-line tool for managing a personal budget. The tool should support the following commands: add a new expense, view all expenses, update an expense, delete an expense, and generate a summary report. Each expense should have an ID, amount, category, date, and description."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate technical documentation based on the given software specification:

Software Specification: {t['software_spec']}

Ensure the documentation includes the following sections:
1. Introduction: Brief overview of the software and its purpose.
2. API/Command Overview: List of endpoints/commands with a brief description.
3. Endpoints/Commands: Detailed descriptions and examples for each endpoint/command, including request and response formats.
4. Data Models: Description of the data structures used, including fields and data types.
5. Error Handling: Explanation of possible errors and their meanings.
6. Usage Examples: Practical examples demonstrating how to use the API/commands.

The documentation should be clear, well-structured, and comprehensive. Use Markdown format for the documentation. Submit your documentation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The documentation should be clear and well-structured.",
            "The documentation should include all required sections.",
            "The documentation should accurately describe the software specification.",
            "The examples should be relevant, detailed, and correctly formatted.",
            "The documentation should be in Markdown format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
