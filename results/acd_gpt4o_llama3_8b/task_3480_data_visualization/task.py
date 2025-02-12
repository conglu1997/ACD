class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": [
                    {"category": "A", "value": 30},
                    {"category": "B", "value": 20},
                    {"category": "C", "value": 50}
                ],
                "description": "Generate a bar chart based on the given data."
            },
            "2": {
                "description": "Interpret the following line chart description and provide insights:\n\nThe chart shows the monthly sales data for a company over a year. Sales started at 100 units in January and increased steadily by 10 units each month until June. From July, sales dropped by 5 units each month until December."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "data" in t:
            return f"""{t['description']}\n\nData:\n{t['data']}\n\nGenerate the visualization as a plain text description of the chart elements and their relationships. Use the following format:\n\n- Chart Type: [Type of chart]\n- Elements: [List of elements with their properties]\n\nExample:\n- Chart Type: Bar Chart\n- Elements:\n  - A: 30\n  - B: 20\n  - C: 50"""
        else:
            return f"""{t['description']}\n\nProvide detailed insights based on the described trends in the data. Use the following format:\n\n- Insights: [Your insights]\n\nExample:\n- Insights: Sales increased steadily from January to June, peaking at 150 units. From July, sales started to decline, ending at 120 units in December. Overall, the trend shows a rise in sales followed by a gradual decline."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "data" in t:
            validation_criteria = [
                "The chart type should be correctly identified.",
                "The elements and their values should be correctly represented.",
                "The description should match the given data."
            ]
        else:
            validation_criteria = [
                "The insights should accurately reflect the described trends in the data.",
                "The monthly changes in sales should be correctly interpreted.",
                "The overall trend should be correctly summarized."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
