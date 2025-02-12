class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "prediction", "events": ["Event 1: Company A launched a new product in Q1.", "Event 2: The product received positive reviews in Q2.", "Event 3: Sales increased by 20% in Q3.", "Event 4: Competitor B released a similar product in Q4.", "Event 5: Company A announced a major update for their product in Q1 next year."], "trend": "Based on these events, predict the market share of Company A by the end of Q1 next year."},
            "2": {"type": "analysis", "scenario": "A town experienced the following events over the past year: a new shopping mall opened in January, a series of community events were held in the summer, a natural disaster occurred in the fall, and a new public transportation system was introduced in December. Additionally, a new tech company started operations in February and a major highway was constructed near the town in August.", "task": "Analyze how these events might have affected the town's population growth and economic development, and predict trends for the next year."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "prediction":
            return f"""Analyze the following sequence of events and predict the future outcome based on the provided trend:\n\nEvents: {', '.join(t['events'])}\n\nTrend: {t['trend']}\n\nSubmit your prediction as a plain text string in the following format:\n\nPrediction: [Your prediction here]"""
        elif t["type"] == "analysis":
            return f"""Analyze the scenario and predict future trends based on the provided events:\n\nScenario: {t['scenario']}\n\nTask: {t['task']}\n\nSubmit your analysis and predictions as a plain text string in the following format:\n\nAnalysis: [Your analysis here]\nPrediction: [Your prediction here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "prediction":
            criteria = ["The prediction should logically follow from the sequence of events.", "The prediction should be plausible and based on the provided trend.", "The prediction should consider the impact of the competitor's product and the major update announced by Company A."]
        elif t["type"] == "analysis":
            criteria = ["The analysis should consider all provided events.", "The prediction should be supported by the analysis.", "The analysis should account for the impact of the new tech company and the major highway construction."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
