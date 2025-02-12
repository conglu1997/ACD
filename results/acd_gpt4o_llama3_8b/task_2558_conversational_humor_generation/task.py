class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "Person A: Why did the chicken cross the road?\nPerson B: I don't know, why?\nPerson A:"
            },
            "2": {
                "context": "Person A: What do you call a bear with no teeth?\nPerson B: I'm not sure, what?\nPerson A:"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous response to complete the following conversation. Ensure your response is contextually relevant and funny.\n\n{t['context']}\n\nSubmit your response as a plain text string in the format:\n\nPerson A: [Your response]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be contextually relevant.",
            "The response should be humorous.",
            "The response should logically follow the given conversation.",
            "The response should be original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
