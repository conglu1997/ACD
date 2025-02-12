class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A hurricane is forecasted to make landfall in a coastal city in 48 hours. Plan an emergency response to ensure the safety of the residents and minimize damage."},
            "2": {"scenario": "A chemical spill has occurred in a densely populated urban area. Plan an emergency response to contain the spill and protect the residents."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with an emergency scenario. Your task is to plan a detailed emergency response to manage the situation effectively. Your plan should include the following elements:
1. Immediate actions to be taken within the first hour.
2. Steps to be taken within the next 24 hours.
3. Resources and personnel needed for the response.
4. Communication strategy to inform and instruct the public.

Scenario:
{t['scenario']}

Example response format:
1. Immediate Actions: [List of actions]
2. Next 24 Hours: [List of steps]
3. Resources: [List of resources and personnel]
4. Communication Strategy: [Communication plan]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The immediate actions should address the most urgent aspects of the scenario.",
            "The steps for the next 24 hours should be logical and aim to manage the situation effectively.",
            "The listed resources and personnel should be appropriate for the scenario.",
            "The communication strategy should be clear and ensure public safety." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
