class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "table_to_text",
                "table": "| Name | Age | Occupation | Location |\n| John | 30  | Engineer   | New York |\n| Mary | 25  | Designer   | San Francisco |\n| Mike | 35  | Manager    | Chicago |\n| Lisa | 28  | Developer  | Austin |"
            },
            "2": {
                "task": "text_to_table",
                "text": "Name: John, Age: 30, Occupation: Engineer, Location: New York. Name: Mary, Age: 25, Occupation: Designer, Location: San Francisco. Name: Mike, Age: 35, Occupation: Manager, Location: Chicago. Name: Lisa, Age: 28, Occupation: Developer, Location: Austin."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "table_to_text":
            return f"""Convert the following table into a textual summary with full sentences. Each entry should be described in a separate sentence:\n{t["table"]}"""
        elif t["task"] == "text_to_table":
            return f"""Convert the following textual information into a table format. Each attribute should be in a separate column in the table:\n{t["text"]}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "table_to_text":
            criteria = ["The response should accurately summarize the tabular data in complete sentences.", "Each entry should be described in a separate sentence."]
        elif t["task"] == "text_to_table":
            criteria = ["The response should accurately convert the textual information into a structured table.", "Each attribute should be in a separate column in the table."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
