class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Write a funny story about a day in the life of a talking cat who goes to work at an office where everyone thinks it's normal.", "description": "Generate a humorous story based on the given scenario."},
            "2": {"scenario": "Create a humorous conversation between two aliens trying to understand human customs, specifically why humans have different types of handshakes.", "description": "Generate a funny conversation based on the given scenario."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        description = t["description"]
        instructions = f"""Your task is to generate humorous content based on the following scenario:\n\nScenario:\n{scenario}\n\nDescription:\n{description}\n\nEnsure that your response is funny, creative, and coherent. Provide your submission in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be humorous and creative.",
            "The response should be coherent and follow the given scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
