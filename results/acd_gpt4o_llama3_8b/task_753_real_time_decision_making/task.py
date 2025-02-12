class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_scenario": "You are the manager of a small restaurant. It's a busy Friday night, and you just got a call that two of your kitchen staff are sick and can't come in. You need to make decisions on how to handle the situation to keep the restaurant running smoothly.",
                "additional_info": [
                    "After 10 minutes, you receive a large order from a corporate client.",
                    "10 minutes later, one of the waitstaff informs you that they broke a leg and can't work the rest of the shift."
                ]
            },
            "2": {
                "initial_scenario": "You are the captain of a spaceship on a mission to explore a newly discovered planet. Suddenly, your navigation system fails, and you need to make decisions to ensure the safety of your crew and the success of the mission.",
                "additional_info": [
                    "After 15 minutes, you discover that the planet's atmosphere contains a harmful gas not detected earlier.",
                    "15 minutes later, you receive a distress signal from a nearby spaceship in need of immediate assistance."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are required to make real-time decisions based on the following scenario:

Initial Scenario: {t['initial_scenario']}

As the scenario progresses, you will receive additional information. You need to adapt your strategy and make decisions to address the changes. Your response should be coherent, logical, and demonstrate effective decision-making under constraints. Submit your response as a plain text string with the following format:

1. Initial Decision: [Your decision based on the initial scenario]
2. Adapted Decision 1: [Your decision after the first piece of additional information]
3. Adapted Decision 2: [Your decision after the second piece of additional information]

Make sure that each decision is detailed, explaining the rationale behind it, and how it addresses the scenario presented."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The initial decision should be logical and address the initial scenario.",
            "Each adapted decision should logically follow from the new information introduced.",
            "The overall strategy should demonstrate effective decision-making under constraints.",
            "Each decision should include a detailed explanation and rationale."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
