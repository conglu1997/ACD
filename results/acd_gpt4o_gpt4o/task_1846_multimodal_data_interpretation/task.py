class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "text": "The company's revenue has been increasing over the past few years due to their expansion into new markets and innovative product lines.",
                "table": "Year, Revenue (in millions)\n2018, 50\n2019, 75\n2020, 120\n2021, 180",
                "question": "What trends can be observed from the data and text, and what might be contributing to these trends?"
            },
            "2": {
                "text": "The weather patterns in the region have shown significant variability, affecting agricultural output and water resources.",
                "table": "Year, Rainfall (in mm), Temperature (°C)\n2017, 500, 22\n2018, 450, 23.5\n2019, 600, 21\n2020, 700, 20",
                "question": "How have the weather patterns impacted agriculture, and what insights can be drawn from the data?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and synthesize information from the following text and table. Provide a comprehensive insight that answers the given question based on both data sources.

Text:
{t['text']}

Table:
{t['table']}

Question:
{t['question']}

Response Format:
Your response should be structured in the following format:
1. Identify key trends observed from the table.
2. Explain how the text supports or provides context to these trends.
3. Provide a comprehensive insight that answers the question."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately integrate information from both the text and the table.",
            "The response should provide a comprehensive insight that answers the question.",
            "The interpretation should be logical and consistent with the data provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
