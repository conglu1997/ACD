class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "The party of the first part shall forthwith assign all rights, title, and interest in and to the Intellectual Property to the party of the second part upon the execution of this Agreement."},
            "2": {"text": "Notwithstanding anything to the contrary contained herein, the Company shall not be liable for any consequential, incidental, or punitive damages arising out of or related to this Agreement, whether in contract, tort, or otherwise."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        text = t["text"]
        return f"""Simplify the following legal language into layman's terms. Ensure your explanation is clear, concise, and easily understandable by someone with no legal background. Avoid using legal jargon and focus on conveying the meaning accurately.

Legal Language: {text}

Submit your response as a plain text string in the following format:

Simplified Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and concise.",
            "The explanation should accurately convey the meaning of the legal language.",
            "The explanation should avoid using legal jargon.",
            "The explanation should be easily understandable by someone with no legal background."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
