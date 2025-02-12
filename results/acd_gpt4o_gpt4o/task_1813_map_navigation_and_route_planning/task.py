class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"map": "A-B-C; B-D; C-D; D-E", "constraints": "Find the shortest route from A to E passing through B and avoiding C."},
            "2": {"map": "P-Q-R; Q-S; R-S; S-T-U", "constraints": "Find a route from P to U that passes through R and T and avoids S."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed route plan based on the following map and constraints:

Map: {t['map']}
Constraints: {t['constraints']}

The map is represented as a series of connections between points, where each connection is indicated with a dash (e.g., A-B means there is a direct path from A to B). A semicolon separates different sets of connections.

Your route plan should include:
1. A clear list of steps from the starting point to the destination.
2. An explanation of why this route satisfies the constraints and is the most efficient.

Ensure your route plan is clear and accurately follows the given constraints. Provide your response in plain text format. Label each section clearly as 'Route Plan' and 'Explanation'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The route should follow the given constraints.", "The explanation should justify the route chosen."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
