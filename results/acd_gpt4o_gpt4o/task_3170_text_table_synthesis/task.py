class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "The sales department has been facing challenges this quarter. The following table shows the sales figures for the past four months.",
                "table": "Month, Sales (in USD)\nJanuary, 12000\nFebruary, 15000\nMarch, 9000\nApril, 11000"
            },
            "2": {
                "text": "Our customer support team received mixed feedback from customers. The table below summarizes the feedback ratings over the last six months.",
                "table": "Month, Rating (out of 5)\nJanuary, 4.2\nFebruary, 3.8\nMarch, 4.0\nApril, 3.5\nMay, 4.1\nJune, 3.9"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a summary based on the following textual description and the accompanying table.

Text: {t['text']}

Table:
{t['table']}

Your summary should:
1. Accurately reflect the key points in the text.
2. Incorporate relevant data from the table.
3. Provide coherent insights or conclusions based on the combined information.

Format your response in plain text as follows:

Summary:
[your summary here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should accurately reflect the key points in the text.",
            "The summary should incorporate relevant data from the table.",
            "The summary should provide coherent insights or conclusions based on the combined information."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
