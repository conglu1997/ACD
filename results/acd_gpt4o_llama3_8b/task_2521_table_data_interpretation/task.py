class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "table": "| Name       | Age | Department | Salary  |\n|------------|-----|------------|---------|\n| Alice      | 30  | HR         | 50000   |\n| Bob        | 25  | Engineering| 60000   |\n| Charlie    | 35  | Marketing  | 55000   |\n| Diana      | 28  | HR         | 52000   |\n| Edward     | 40  | Engineering| 70000   |"
            },
            "2": {
                "table": "| Product    | Sales_Q1 | Sales_Q2 | Sales_Q3 | Sales_Q4 |\n|------------|---------|---------|---------|---------|\n| Product A  | 500     | 700     | 600     | 800     |\n| Product B  | 400     | 600     | 500     | 700     |\n| Product C  | 300     | 400     | 350     | 450     |\n| Product D  | 200     | 300     | 250     | 350     |"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the data from the following table and generate a textual summary. Your summary should include key points and insights derived from the data. Ensure your summary is coherent, concise, and captures the main information presented in the table. The summary should be between 100-150 words long. Submit your summary as a plain text string.\n\n{t['table']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The summary should be coherent and concise.", "The summary should capture the main information presented in the table.", "The summary should include key points and insights derived from the data.", "The summary should be between 100-150 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
