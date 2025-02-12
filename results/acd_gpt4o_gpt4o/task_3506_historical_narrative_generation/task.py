class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Declaration of Independence in 1776.", "context": "Describe the atmosphere in the room, the key figures involved, and the significance of this event."},
            "2": {"event": "The fall of the Berlin Wall in 1989.", "context": "Describe the scene at the Berlin Wall, the emotions of the people present, and the significance of this event."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to generate a narrative based on the given historical event. Ensure that your narrative is historically accurate, contextually rich, and coherent. The narrative should include detailed descriptions of the atmosphere, key figures involved, and the significance of the event. Format your response as follows:

1. Event: [The given historical event]
2. Narrative:
[Your narrative describing the event, the atmosphere, key figures, and its significance]
""".format(t["event"], t["context"])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The narrative should be historically accurate, contextually rich, and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
