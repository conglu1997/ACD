class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A company produces different types of widgets. The table below shows the production cost and selling price for each type of widget. Based on this data, you need to determine which widget type yields the highest profit margin.",
                "table": "| Widget Type | Production Cost | Selling Price |\n|-------------|----------------|---------------|\n| Widget A    | $5             | $10           |\n| Widget B    | $7             | $14           |\n| Widget C    | $6             | $12           |",
                "question": "Which widget type yields the highest profit margin?"
            },
            "2": {
                "description": "A small farm tracks the daily milk production and feed consumption for its cows. The table below shows the data for the past week. Using this data, determine on which day the feed consumption per liter of milk was the lowest.",
                "table": "| Day       | Milk Production (liters) | Feed Consumption (kg) |\n|-----------|---------------------------|-----------------------|\n| Monday    | 50                        | 30                    |\n| Tuesday   | 45                        | 28                    |\n| Wednesday | 55                        | 32                    |\n| Thursday  | 60                        | 35                    |\n| Friday    | 58                        | 33                    |\n| Saturday  | 62                        | 34                    |\n| Sunday    | 48                        | 29                    |",
                "question": "On which day was the feed consumption per liter of milk the lowest?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following information from both the textual description and the table provided. Based on this information, answer the question provided.

Description: {t['description']}

Table:
{t['table']}

Question: {t['question']}

Provide your response in plain text format as follows:
Answer: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly interpret the information from both the textual description and the table.", "The response should accurately answer the question based on the data provided.", "The calculations involved in deriving the answer should be correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
