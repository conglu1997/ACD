class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Something you can catch but can't throw."},
            "2": {"prompt": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a riddle based on the following prompt and provide its solution:

Prompt: {t['prompt']}

Ensure the riddle is engaging, challenging, and makes sense within the context of the prompt. The riddle should be concise and thought-provoking. Provide the riddle and its solution in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The riddle should be engaging.", "The riddle should be challenging.", "The riddle should make sense within the context of the prompt.", "The riddle should be concise and thought-provoking.", "The solution should be correct and logically follow from the riddle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
