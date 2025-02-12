class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "abstract": "This study investigates the impact of different fertilizers on crop yield. Three types of fertilizers (A, B, and C) were tested over six months. Fertilizer A showed a 15% increase in yield, Fertilizer B showed a 20% increase, and Fertilizer C showed a 10% increase.",
                "data": {
                    "fertilizers": ["A", "B", "C"],
                    "yield_increase": [15, 20, 10]
                }
            },
            "2": {
                "abstract": "The research explores the effects of different study techniques on exam performance. Three techniques (X, Y, and Z) were analyzed over a semester. Technique X improved scores by 5%, Technique Y by 10%, and Technique Z by 8%.",
                "data": {
                    "techniques": ["X", "Y", "Z"],
                    "score_increase": [5, 10, 8]
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given research paper abstract and data:

Abstract: {t["abstract"]}

Tasks:
1. Summarize the key findings of the research paper.
2. Generate a Python code snippet to create a visual representation (e.g., bar chart) of the data provided.
3. Describe any potential implications or insights that can be drawn from the data.

Submit your response as a plain text string with sections for 'Summary', 'Visualization Code', and 'Implications'. Include the Python code for generating the visualization in the 'Visualization Code' section.

Example format:
Summary: [Your summary here]
Visualization Code: [Your Python code here]
Implications: [Your implications here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should accurately reflect the key findings of the research paper.",
            "The visualization code should correctly generate a chart that matches the data provided.",
            "The implications should be coherent, insightful, and logically derived from the data."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
