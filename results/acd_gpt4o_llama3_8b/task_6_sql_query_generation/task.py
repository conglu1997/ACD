class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "schema": "CREATE TABLE employees (id INT, name VARCHAR(100), department VARCHAR(100), salary INT);",
                "requirement": "Write a SQL query to find the names of employees who work in the 'Sales' department and have a salary greater than 50000."
            },
            "2": {
                "schema": "CREATE TABLE products (id INT, name VARCHAR(100), price DECIMAL, stock INT); CREATE TABLE orders (id INT, product_id INT, quantity INT);",
                "requirement": "Write a SQL query to find the names of products that have been ordered more than 10 times."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a SQL query based on the given database schema and requirement: 

Schema:
{t['schema']}

Requirement:
{t['requirement']}

Ensure the SQL query is syntactically correct and meets the specified requirements."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The SQL query should be syntactically correct.", "The query should meet the given requirement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
