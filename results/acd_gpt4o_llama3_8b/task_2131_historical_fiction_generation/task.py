class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Berlin Wall in 1989."},
            "2": {"event": "The signing of the Declaration of Independence in 1776."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        historical_event = t['event']
        return f"Generate a fictional narrative that takes place during the following historical event: {historical_event}. Ensure that your narrative is plausible within the historical context, includes at least one main character, and incorporates key facts about the event. Submit your narrative as a plain text string in the following format:\n\nNarrative: [Your narrative here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The narrative should be plausible within the historical context.",
            "The narrative should include at least one main character.",
            "The narrative should incorporate key facts about the historical event.",
            "The narrative should be coherent and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
