class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirement": "Generate an SQL query to find the names, departments, and hire dates of all employees in the 'employees' table who have a salary greater than $50,000 and were hired after January 1, 2010.", "table_schema": "CREATE TABLE employees (id INT, name VARCHAR(255), department VARCHAR(255), salary INT, hire_date DATE);"},
            "2": {"query": "SELECT department, SUM(salary) FROM employees WHERE hire_date > '2015-01-01' GROUP BY department;", "expected_output": "department | SUM(salary)\n-----------|------------\nHR         | 135000\nEngineering| 375000\nMarketing  | 110000"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "requirement" in t:
            instructions = f"Your task is to generate an SQL query based on the following requirement:\n\nRequirement: {t['requirement']}\n\nTable Schema: {t['table_schema']}\n\nEnsure that your query is syntactically correct and meets the requirement. Provide your query in plain text format, with each clause on a new line."
        else:
            instructions = f"Your task is to interpret the output of the following SQL query:\n\nQuery: {t['query']}\n\nExpected Output:\n{t['expected_output']}\n\nProvide a brief explanation of what the query does and what the output means. Provide your explanation in plain text format, structured as follows:\n1. Query Purpose: [Your explanation of the query's purpose]\n2. Output Interpretation: [Your interpretation of the output]"
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "requirement" in t:
            criteria = ["The query should correctly find the names, departments, and hire dates of employees with a salary greater than $50,000 and hired after January 1, 2010.", "The query should be syntactically correct."]
        else:
            criteria = ["The explanation should accurately describe the purpose of the query.", "The explanation should correctly interpret the output provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
