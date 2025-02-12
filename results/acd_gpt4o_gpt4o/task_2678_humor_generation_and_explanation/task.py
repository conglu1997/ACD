class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the scarecrow win an award?"},
            "2": {"prompt": "Why don't scientists trust atoms?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following prompt, generate an original humorous response and explain why it is funny. Ensure that the humor is appropriate and culturally sensitive.

Prompt:
- {t['prompt']}

Your response should be in plain text format as follows:

Response: [Your original humorous response here]
Explanation: [Your explanation of why it is funny here, including a detailed analysis of the humor elements (e.g., wordplay, irony, cultural references).]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should be humorous and appropriate.",
            "The response should be original and not a well-known joke.",
            "The explanation should clearly articulate why the response is funny, including a detailed analysis of the humor elements (e.g., wordplay, irony, cultural references)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
