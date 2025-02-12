class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event1": "The signing of the Magna Carta in 1215.", "event2": "The American Declaration of Independence in 1776."},
            "2": {"event1": "The fall of the Western Roman Empire in 476.", "event2": "The rise of the Renaissance in the 14th century."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and describe the connections between the following historical events. Consider their causes, consequences, and any other relevant factors in your explanation. Ensure your response is clear, logical, and based on historical facts.

Event 1: {t['event1']}
Event 2: {t['event2']}

Provide your response in the following format:

Connection: [Description of the connection]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear and logical description of the connection between the events.", "The explanation should be based on historical facts and consider relevant factors."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
