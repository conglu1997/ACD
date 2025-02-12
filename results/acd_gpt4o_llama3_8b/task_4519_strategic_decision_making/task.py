class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are leading a team in a resource-management game. Your goal is to collect 10 units of resources within 5 turns. Each turn, you can choose one action: 'Gather' to collect 2 units, 'Build' to construct a structure that doubles the resources gathered in the next turn, or 'Rest' to skip a turn and reduce the risk of failure in the next turn. Note that 'Build' takes one turn to complete before it becomes effective, and 'Rest' restores any penalties from previous turns. Be mindful of the sequence and combination of actions to optimize resource collection.", "task_type": "resource_management"},
            "2": {"scenario": "You are a commander in a turn-based strategy game. Your goal is to capture the enemy's base within 5 turns. Each turn, you can choose one action: 'Advance' to move closer to the enemy base, 'Defend' to fortify your current position, or 'Scout' to gather intelligence on enemy movements. Note that 'Advance' and 'Defend' have varying probabilities of success based on the previous actions taken, and 'Scout' provides information that can influence your subsequent decisions. Plan your actions strategically to ensure a successful capture within the given turns.", "task_type": "strategy_game"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario:

Scenario: {t['scenario']}

Your response should include:
1. A description of each action you choose for each turn.
2. The rationale behind each decision.
3. The outcome of each action.

Submit your response as a plain text string in the following format:

Turn 1: [Action]
Rationale: [Reason for choosing the action]
Outcome: [Result of the action]

Turn 2: [Action]
Rationale: [Reason for choosing the action]
Outcome: [Result of the action]

...(repeat for all turns)...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a description of each action chosen for each turn.",
            "The response should include the rationale behind each decision.",
            "The response should include the outcome of each action.",
            "The response should logically lead to achieving the goal specified in the scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
