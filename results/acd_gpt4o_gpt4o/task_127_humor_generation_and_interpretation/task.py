class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the scarecrow win an award?"},
            "2": {"scenario": "Two programmers are having a conversation about debugging."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a humorous punchline for the following prompt:

{t['prompt']}

Provide your response in a single sentence."""
        elif "scenario" in t:
            instructions = f"""Your task is to generate a humorous dialogue based on the following scenario:

{t['scenario']}

Ensure the dialogue is funny, context-appropriate, and maintains a consistent tone. The conversation should be at least 5 exchanges long, with each character contributing to the dialogue. Provide the dialogue in plain text format without additional formatting."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be humorous.", "The response should be context-appropriate.", "The response should maintain a consistent tone.", "The humor should be relevant to the given prompt or scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
