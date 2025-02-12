class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instruction": "Generate a data table with the following criteria:\n\n1. The table should represent the monthly sales of a product across four regions (North, South, East, West) for the year 2022.\n2. Each row should represent a month, and each column should represent a region.\n3. Fill the table with realistic fictitious sales figures.\n4. Ensure that the table is formatted as plain text using commas as delimiters.\n\nProvide your response in the following format:\n\nMonth,North,South,East,West\nJanuary,100,200,150,175\n...\nDecember,110,190,140,165\n", "criteria": ["The table should have 12 rows (one for each month) and 4 columns (one for each region)", "The sales figures should be realistic and varied", "The table should be formatted as plain text with appropriate headers"]},
            "2": {"instruction": "Interpret the following data table and answer the questions provided:\n\n| Month    | North | South | East | West |\n|----------|-------|-------|------|------|\n| January  | 120   | 135   | 150  | 110  |\n| February | 130   | 145   | 160  | 120  |\n| March    | 140   | 155   | 170  | 130  |\n| April    | 150   | 165   | 180  | 140  |\n| May      | 160   | 175   | 190  | 150  |\n| June     | 170   | 185   | 200  | 160  |\n| July     | 180   | 195   | 210  | 170  |\n| August   | 190   | 205   | 220  | 180  |\n| September| 200   | 215   | 230  | 190  |\n| October  | 210   | 225   | 240  | 200  |\n| November | 220   | 235   | 250  | 210  |\n| December | 230   | 245   | 260  | 220  |\n\nQuestions:\n1. Which month had the highest sales in the North region?\n2. What is the total sales for the East region in the year?\n3. Calculate the average monthly sales in the South region.\n\nProvide your answers in the following format:\n\n1. [Your answer]\n2. [Your answer]\n3. [Your answer]", "criteria": ["Correctly identify the month with the highest sales in the North region", "Accurately calculate the total sales for the East region", "Correctly calculate the average monthly sales in the South region"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['instruction']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get('criteria', [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
