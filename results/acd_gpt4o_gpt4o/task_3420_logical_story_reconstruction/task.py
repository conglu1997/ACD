class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": ["Alice found a mysterious key.", "She opened the old chest in her attic.", "Inside, she discovered a map.", "The map led to a hidden treasure."]},
            "2": {"events": ["The scientist made a groundbreaking discovery.", "The experiment was a success.", "He received a prestigious award.", "His research changed the world."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events = t["events"]
        instructions = f"""Your task is to reconstruct a coherent story from the following set of disjointed sentences or events:\n\n{events}\n\nEnsure that the story is logically consistent, temporally ordered, and coherent. Provide your response in plain text format as a single, well-structured narrative."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be logically consistent.", "The story should be temporally ordered.", "The story should be coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
