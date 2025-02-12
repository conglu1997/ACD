class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The signing of the Declaration of Independence in 1776",
                "figure": "Thomas Jefferson"
            },
            "2": {
                "event": "The fall of the Berlin Wall in 1989",
                "figure": "Mikhail Gorbachev"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical event from the perspective of the specified historical figure:

Event: {t['event']}
Historical Figure: {t['figure']}

Your analysis should include the following components:
1. An introduction to the event and its historical context.
2. A detailed perspective of the specified historical figure, considering their personal views, motivations, and actions during the event.
3. An analysis of the impact and significance of the event from the figure's viewpoint.

Ensure your response is well-organized, coherent, and provides insightful analysis. Your response should be between 300 to 500 words. Submit your response as a plain text string with the following sections:

1. Introduction: [Introduce the event and its context]
2. Perspective: [Provide the historical figure's perspective]
3. Analysis: [Analyze the impact and significance of the event from the figure's viewpoint]

Example Format:

Introduction: [Your introduction here]
Perspective: [Your perspective here]
Analysis: [Your analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should address the specified historical event and figure.",
            "The perspective should be coherent and well-organized.",
            "The analysis should provide insights into the event and the figure's viewpoint."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
