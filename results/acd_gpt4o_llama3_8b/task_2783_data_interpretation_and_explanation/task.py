class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"chart": "Year,Sales\n2015,200\n2016,240\n2017,300\n2018,310\n2019,450", "questions": ["What is the general trend of sales from 2015 to 2019?", "Identify any significant changes in sales and provide possible reasons for those changes."]},
            "2": {"chart": "Month,Temperature\nJanuary,5\nFebruary,7\nMarch,12\nApril,15\nMay,20\nJune,25\nJuly,30\nAugust,28\nSeptember,22\nOctober,16\nNovember,10\nDecember,6", "questions": ["Describe the overall temperature trend throughout the year.", "Which months show the highest and lowest temperatures, and what might be the reasons for these variations?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        chart = t["chart"]
        questions = "\n".join(t["questions"])
        return f"""Interpret the data from the following chart or graph and provide detailed answers to the specified questions.\nChart:\n{chart}\nQuestions:\n{questions}\nEnsure your explanations are clear, accurate, and provide insights based on the data. Submit your answers as a plain text string with each answer on a new line, labeled with the respective question number."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
