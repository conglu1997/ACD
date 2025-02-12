class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Roman Empire"},
            "2": {"event": "The signing of the Declaration of Independence"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given event:

{t["event"]}

Reconstruct a detailed historical narrative of this event. Your narrative should include:
1. The historical context leading up to the event.
2. The key figures involved and their roles.
3. The main events and their chronological order.
4. The immediate and long-term consequences of the event.

Ensure your narrative is coherent, factually accurate, and well-structured. Submit your response as a plain text string in paragraph format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should include historical context, key figures, main events in chronological order, and consequences.", "The narrative should be coherent, factually accurate, and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
