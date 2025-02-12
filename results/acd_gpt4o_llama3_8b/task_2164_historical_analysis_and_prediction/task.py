class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The Industrial Revolution",
                "context": "Analyze the key factors that led to the Industrial Revolution, such as technological innovation, population growth, and economic changes. Predict how similar factors could influence future technological advancements in the context of current trends like artificial intelligence and renewable energy."
            },
            "2": {
                "historical_event": "The Fall of the Roman Empire",
                "context": "Examine the causes of the fall of the Roman Empire, including political instability, economic troubles, and external invasions. Predict what modern empires or nations might face similar challenges, considering factors such as political polarization, economic inequality, and geopolitical tensions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        historical_event = t["historical_event"]
        context = t["context"]
        return f"""Analyze the following historical event and make predictions based on historical trends. Historical Event: {historical_event}\n
Context: {context}\n
Submit your analysis and predictions as a plain text string in the following format: 'Analysis: [Your analysis]\nPrediction: [Your prediction]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should be accurate and well-reasoned.", "The prediction should logically follow from the analysis and context provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
