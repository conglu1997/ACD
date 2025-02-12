class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Three friends (Alice, Bob, and Carol) are planning a weekend trip. They have different preferences: Alice likes hiking, Bob prefers the beach, and Carol enjoys cultural activities. Generate a dialogue among them as they discuss and decide on their weekend plans."},
            "2": {"scenario": "Two colleagues (Emma and John) are working on a project with a tight deadline. Emma is detail-oriented but slow, while John is fast but prone to mistakes. Generate a dialogue between them as they try to come up with a plan to meet the deadline."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Generate a coherent and logical dialogue based on the following scenario:

{scenario}

Ensure that the dialogue is natural, each character's voice is consistent, and the conversation logically progresses towards a resolution. Submit your dialogue as a plain text string in the following format:

Alice: [Alice's dialogue]
Bob: [Bob's dialogue]
Carol: [Carol's dialogue]
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be natural and coherent.",
            "Each character's voice should be consistent.",
            "The conversation should logically progress towards a resolution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
