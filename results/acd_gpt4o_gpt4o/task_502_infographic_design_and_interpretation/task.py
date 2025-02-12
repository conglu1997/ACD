class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": [{"category": "A", "value": 25}, {"category": "B", "value": 45}, {"category": "C", "value": 15}, {"category": "D", "value": 10}, {"category": "E", "value": 5}], "description": "Design an infographic to represent the percentage distribution of five categories: A, B, C, D, and E."},
            "2": {"infographic": "A pie chart with five slices labeled A, B, C, D, and E with proportions representing 25%, 45%, 15%, 10%, and 5% respectively. The pie chart has a legend and is titled 'Category Distribution'.", "description": "Interpret the infographic to explain the percentage distribution of categories A, B, C, D, and E."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'data' in t:
            return f"""Your task is to design an infographic based on the provided data.

Data: {t['data']}

Ensure your infographic includes:
1. A clear title.
2. Visual elements (e.g., bar chart, pie chart) to represent the data accurately.
3. Labels and legends to explain the data.

Provide a detailed description of your infographic in plain text format.

Example response format:
Title: [Your title here]
Description: [Your description of the infographic here, including visual elements and labels]
"""
        else:
            return f"""Your task is to interpret the given infographic to explain the key information.

Infographic: {t['infographic']}

Ensure your interpretation includes:
1. Explanation of the visual elements.
2. Extraction of key data points.
3. A clear and concise summary of the information presented.

Provide your interpretation in plain text format.

Example response format:
Explanation: [Your explanation of the visual elements here]
Key Data Points: [Extracted key data points here]
Summary: [Your summary here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = None
        if 'data' in t:
            criteria = ["The description should include a clear title.", "Visual elements should accurately represent the data.", "Labels and legends should explain the data clearly.", "The distribution of percentages should be accurate."]
        else:
            criteria = ["The interpretation should explain the visual elements.", "Key data points should be extracted accurately.", "The summary should be clear and concise.", "The interpretation should match the given infographic."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
