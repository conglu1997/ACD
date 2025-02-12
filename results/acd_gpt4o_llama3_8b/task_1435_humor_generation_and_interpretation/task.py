class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a humorous short story about a day in the life of a talking cat.", "type": "generation"},
            "2": {"joke": "Why don’t scientists trust atoms? Because they make up everything.", "type": "interpretation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generation":
            return f"""Generate a humorous short story based on the following prompt: '{t["prompt"]}'. Ensure that the story is engaging, coherent, and funny. Submit your response as a plain text string in the following format:

Story: [Your story here]"""
        else:
            return f"""Interpret the following joke and explain why it is humorous: '{t["joke"]}'. Ensure that your explanation is clear and covers the elements that make the joke funny. Submit your response as a plain text string in the following format:

Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generation":
            criteria = ["The story should be humorous, engaging, and coherent."]
        else:
            criteria = ["The explanation should clearly describe why the joke is humorous and cover the elements that make it funny."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
