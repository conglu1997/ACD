class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "table": "Year, Sales, Profit\n2018, 1000, 200\n2019, 1100, 220\n2020, 900, 180\n2021, 1200, 240\n2022, 1150, 230\n2023, 1250, 250",
                "question": "Analyze the given table and describe the trend in sales and profit over the years. What can you infer about the business performance?"
            },
            "2": {
                "table": "Quarter, Product_A, Product_B, Product_C\nQ1, 300, 450, 200\nQ2, 320, 460, 210\nQ3, 310, 470, 220\nQ4, 330, 480, 230\nQ5, 340, 490, 240\nQ6, 350, 500, 250",
                "question": "Based on the given table, predict the sales for each product in the next quarter (Q7). Provide your reasoning for each prediction."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves interpreting and analyzing data from the given table and answering the question provided.\n\nTable:\n{t['table']}\n\nQuestion:\n{t['question']}\n\nProvide your answer in plain text format, structured as follows:\n\nAnalysis/Prediction: [Your analysis or prediction]\nReasoning: [Your reasoning]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly analyze the data and provide a logical and coherent conclusion or prediction.", "The response should include reasoning that is consistent with the data provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
