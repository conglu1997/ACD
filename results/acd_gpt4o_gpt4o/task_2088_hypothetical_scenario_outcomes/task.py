class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "initial_conditions": "You are a scientist who has discovered a new element with unique properties. This element can absorb and release energy at will. Describe the potential scientific, societal, and ethical outcomes of this discovery."
            },
            "2": {
                "initial_conditions": "You are the leader of a small nation that has just found a vast reserve of a rare mineral that is highly sought after globally. Describe the potential economic, political, and environmental outcomes of this discovery."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate and interpret potential outcomes for the following hypothetical scenario based on the given initial conditions. Ensure that your response is detailed, coherent, and considers multiple aspects of the scenario, including scientific, societal, ethical, economic, political, and environmental outcomes where applicable. Provide your response in plain text format.

Initial Conditions: {t['initial_conditions']}

Provide your potential outcomes in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be detailed and coherent.", "The response should consider multiple aspects of the scenario, including scientific, societal, ethical, economic, political, and environmental outcomes where applicable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
