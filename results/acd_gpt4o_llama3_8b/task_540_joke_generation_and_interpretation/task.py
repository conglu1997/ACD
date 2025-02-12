class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the scarecrow win an award?"},
            "2": {"prompt": "Generate a joke about computers."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Complete the following task based on the given prompt:

Prompt: {prompt}

1. If the prompt is a question, provide a humorous answer to the question.
2. If the prompt is a topic, generate a joke related to that topic.

Ensure that the joke is culturally appropriate, logically coherent, and humorous. Submit your response as a plain text string in the following format:

Response: [Your joke]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The joke should be culturally appropriate.", "The joke should be logically coherent.", "The joke should be humorous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
