class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "statement": "I just lost my job and I feel devastated. I don't know how I'm going to support my family now."
            },
            "2": {
                "statement": "I'm feeling incredibly anxious about my upcoming exams. I've been studying so hard, but I'm worried it won't be enough."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        statement = t["statement"]
        instructions = f"""Your task is to recognize the emotion expressed in the following statement and respond empathetically:

{statement}

Your response should:
1. Acknowledge the emotion expressed in the statement.
2. Provide comfort or support that is appropriate for the context.
3. Offer a positive or reassuring message to help the individual cope with their feelings.

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately recognize the emotion expressed in the statement.",
            "The response should provide comfort or support.",
            "The response should be contextually appropriate and empathetic.",
            "The response should offer a positive or reassuring message."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
