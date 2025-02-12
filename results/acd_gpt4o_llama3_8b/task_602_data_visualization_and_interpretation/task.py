class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": [
                    {"month": "January", "sales": 1000},
                    {"month": "February", "sales": 1500},
                    {"month": "March", "sales": 2000},
                    {"month": "April", "sales": 2500},
                    {"month": "May", "sales": 3000},
                    {"month": "June", "sales": 3500},
                    {"month": "July", "sales": 4000},
                    {"month": "August", "sales": 4500},
                    {"month": "September", "sales": 5000},
                    {"month": "October", "sales": 5500},
                    {"month": "November", "sales": 6000},
                    {"month": "December", "sales": 6500}
                ],
                "visualization_type": "line_chart"
            },
            "2": {
                "visualization_description": "A bar chart with the months of the year on the X-axis and sales figures on the Y-axis. The bars for each month are as follows: January - 1000, February - 1500, March - 2000, April - 2500, May - 3000, June - 3500, July - 4000, August - 4500, September - 5000, October - 5500, November - 6000, December - 6500.",
                "question": "What month had the highest sales?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "data" in t:
            return f"""Generate a {t['visualization_type']} based on the following data:

{t['data']}

Ensure the visualization accurately represents the data and is easy to understand. Submit your response as a detailed description of the visualization in plain text, including the title, labels, and a brief explanation of what the visualization shows. Format your response as follows:

Title: [Title]
X-axis Label: [X-axis label]
Y-axis Label: [Y-axis label]
Explanation: [Brief explanation]"""
        else:
            return f"""Interpret the provided bar chart and answer the following question:

{t['visualization_description']}

{t['question']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "data" in t:
            validation_criteria = [
                "The description should include a title for the visualization.",
                "The description should include labels for the axes.",
                "The explanation should accurately describe what the visualization shows."
            ]
        else:
            validation_criteria = [
                "The answer should correctly identify the month with the highest sales based on the provided visualization."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
