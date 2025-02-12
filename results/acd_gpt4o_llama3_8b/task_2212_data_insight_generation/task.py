class TaskFamily:
    import pandas as pd
    import io

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "Name,Age,Salary,Department,Years_at_Company,Performance_Rating\nAlice,34,70000,HR,5,4.5\nBob,45,80000,Engineering,8,4.2\nCharlie,29,50000,Marketing,2,3.8\nDiana,39,65000,HR,6,4.0\nEve,50,90000,Engineering,10,4.7\nFrank,28,45000,Marketing,1,3.5\nGrace,41,72000,HR,7,4.3"},
            "2": {"data": "Product,Sales,Region,Quarter,Profit,Customer_Satisfaction\nA,120,North,Q1,30,4.0\nB,150,South,Q1,40,4.2\nC,100,East,Q1,25,3.8\nD,130,West,Q1,35,4.1\nE,170,North,Q2,50,4.5\nF,160,South,Q2,45,4.3\nG,110,East,Q2,30,4.0\nH,140,West,Q2,38,4.1"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        data = t["data"]
        return f"""Analyze the following dataset and generate meaningful insights and summaries from it. The dataset is:\n\n{data}\n\nYour insights should identify patterns, trends, or anomalies in the data and summarize key findings.\n\nSubmit your insights and summaries as a plain text string in the following format:\n\nInsights: [Your insights and summaries here]\n\nExample:\n\nInsights: Employees in the Engineering department tend to have higher salaries and more years at the company. The North region has the highest sales and customer satisfaction in both Q1 and Q2."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The insights should be meaningful and derived from the dataset.", 
            "The summaries should be coherent and clearly communicated.", 
            "The analysis should reflect a correct understanding of the data."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
