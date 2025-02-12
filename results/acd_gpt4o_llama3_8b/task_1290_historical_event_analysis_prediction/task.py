class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Roman Empire", "hypothetical_scenario": "What if the Roman Empire had successfully repelled the barbarian invasions and maintained its territorial integrity?"},
            "2": {"event": "The Industrial Revolution", "hypothetical_scenario": "What if the Industrial Revolution had begun 100 years earlier and spread more rapidly across continents?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the following historical event and provide your insights or predictions based on the given hypothetical scenario:\nEvent: {t['event']}\nHypothetical Scenario: {t['hypothetical_scenario']}\nYour response should include:\n1. An analysis of the original event, covering key factors and consequences.\n2. Predictions of the potential outcomes based on the hypothetical scenario, considering various aspects such as political, social, and economic impacts.\nProvide your analysis in a clear and concise manner as a plain text string in the following format:\n\nAnalysis: [Your analysis]\nPredictions: [Your predictions]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear and accurate analysis of the original event, covering key factors and consequences, and coherent, logical predictions based on the hypothetical scenario, considering various aspects such as political, social, and economic impacts."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
