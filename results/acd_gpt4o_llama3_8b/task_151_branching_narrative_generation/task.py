class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "starting_point": "You are in a dark forest with two paths ahead. One path leads to a village, and the other leads to a cave.",
                "constraints": "The narrative should include at least three decision points, with at least two options at each decision point, and each option should lead to a different outcome."
            },
            "2": {
                "starting_point": "You find yourself in an abandoned spaceship. There are controls in front of you and a door to your left.",
                "constraints": "The narrative should include at least three decision points, with at least two options at each decision point, and each option should lead to a different outcome."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a branching narrative based on the following starting point and constraints:

Starting Point: {t['starting_point']}

Constraints: {t['constraints']}

Your narrative should include at least three decision points, with at least two options at each decision point, and each option should lead to a different outcome. Ensure that the narrative is coherent and engaging. Structure your narrative in the following format:

1. Initial scenario
2. Decision point 1: Option A, Option B
3. Outcome of Option A
4. Outcome of Option B
5. Decision point 2: Option A, Option B
6. Outcome of Option A
7. Outcome of Option B
...

Submit your narrative as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should include at least three decision points.",
            "Each decision point should have at least two options.",
            "Each option should lead to a different outcome.",
            "The narrative should be coherent and engaging."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
