class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Two coworkers, Alex and Jamie, are in conflict because Alex feels Jamie is not contributing equally to a shared project. Alex has been working late hours to meet deadlines, while Jamie leaves at the regular end of the workday."},
            "2": {"scenario": "A couple, Sam and Taylor, are arguing because Sam frequently forgets to do household chores, which frustrates Taylor. Taylor works from home and feels overwhelmed by the imbalance in responsibilities."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a resolution strategy for the following interpersonal conflict scenario:

Scenario: {t['scenario']}

Your resolution strategy should include the following elements:
1. A brief summary of the main issues.
2. An empathetic approach to understanding both parties' perspectives.
3. A step-by-step plan to address and resolve the conflict.
4. Suggestions for preventing similar conflicts in the future.

Your response should be clear, logical, and demonstrate emotional intelligence. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The strategy includes a summary of the main issues.", "The strategy shows empathy towards both parties.", "The strategy includes a step-by-step plan to resolve the conflict.", "The strategy provides suggestions for preventing future conflicts.", "The strategy is clear, logical, and demonstrates emotional intelligence."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
