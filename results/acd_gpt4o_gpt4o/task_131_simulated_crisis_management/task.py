class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A wildfire is rapidly approaching a small town. You are the emergency response coordinator. There are limited evacuation routes, and the nearest firefighting resources are 30 minutes away. Decide on the immediate actions to take to ensure the safety of the residents."},
            "2": {"scenario": "A sudden flood has hit a city, causing widespread damage and power outages. As the crisis manager, outline the steps you will take in the first 24 hours to manage the situation. Note that communication networks are down, and there is limited access to clean water."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to navigate through the following simulated emergency scenario and make decisions based on the evolving conditions:

Scenario: {t['scenario']}

Outline your immediate actions and the reasoning behind each decision. Consider the safety of the people, the resources available, and the potential long-term impact of your decisions. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should demonstrate clear and logical decision-making.", "The response should consider the safety of the people.", "The response should make effective use of available resources.", "The response should consider the potential long-term impact of the decisions.", "The response should address the specific constraints and evolving conditions mentioned in the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
