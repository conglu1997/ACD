class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A massive earthquake has struck a densely populated urban area. There are reports of widespread building collapses, fires, power outages, and trapped individuals. The local hospital is overwhelmed, and there are limited medical supplies available. You have a team of 10 responders, 3 ambulances, 2 fire trucks, and a limited supply of medical kits. Plan your response, prioritizing actions such as search and rescue, medical aid, and fire control.", "context": "Plan your actions step-by-step, considering the limited resources and the need to save as many lives as possible. Provide your response in a structured format."},
            "2": {"scenario": "A hurricane is approaching a coastal city. There is a mandatory evacuation order, but many residents are refusing to leave. There are reports of flooding in low-lying areas and power outages throughout the city. You have a team of 20 responders, 5 boats, and a limited supply of food and water. Plan your response, prioritizing actions such as evacuation, providing shelter, and ensuring the safety of your team.", "context": "Plan your actions step-by-step, considering the limited resources and the need to ensure the safety of both residents and responders. Provide your response in a structured format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to plan and prioritize actions in the following emergency scenario:\n\nScenario: {t['scenario']}\n\nContext: {t['context']}\n\nEnsure that your plan is detailed, logical, and prioritizes actions effectively based on the given scenario. Provide your response in the following format:\n\n1. Initial Assessment\n2. Planned Actions\n3. Justification for Priorities\n4. Contingency Plans\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include an initial assessment of the situation.", "The planned actions must be detailed and logical.", "The justification for priorities must be clear and reasonable based on the scenario.", "The response should include contingency plans for unexpected developments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
