class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are the commander of a small army in a turn-based strategy game. Your objective is to capture the enemy's base within 10 turns. You have the following units: 5 infantry, 2 archers, and 1 cavalry. The enemy has 4 infantry, 3 archers, and 2 cavalry. The terrain includes a river that can only be crossed at two bridges. Provide a detailed plan for how you will achieve victory, considering unit positioning, movement, and engagement with enemy forces.",
                "constraints": "You must capture the enemy's base within 10 turns. Your units have the following movement ranges: infantry (1 tile/turn), archers (1 tile/turn), cavalry (2 tiles/turn). The river can only be crossed at the bridges, and each bridge can only be crossed by one unit per turn."
            },
            "2": {
                "scenario": "You are the leader of a small colony on a distant planet in a turn-based strategy game. Your objective is to establish a self-sufficient colony within 20 turns. You have the following resources: 100 units of food, 50 units of water, and 30 units of building materials. You also have 5 workers who can perform various tasks such as farming, building, and resource gathering. Provide a detailed plan for how you will achieve self-sufficiency, considering resource management, worker assignments, and construction priorities.",
                "constraints": "You must establish self-sufficiency within 20 turns. Each worker can perform one task per turn. Farming produces 2 units of food per turn, water gathering produces 3 units of water per turn, and building consumes 5 units of building materials per turn."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate the following turn-based strategy game scenario and provide a detailed plan for achieving the objective:

Scenario: {t['scenario']}

Constraints: {t['constraints']}

Ensure that your plan is detailed, logically coherent, and considers all given constraints. Submit your plan as a plain text string.

Response Format:
Plan: [Your detailed plan here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The plan should be detailed and logically coherent.",
            "The plan should consider all given constraints.",
            "The plan should provide a clear path to achieving the objective within the specified number of turns.",
            "Each turn's actions should be specified clearly and logically."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
