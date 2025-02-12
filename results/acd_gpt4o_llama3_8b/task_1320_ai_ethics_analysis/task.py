class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "A company has developed an AI system that can predict criminal behavior with high accuracy. Should the company sell this technology to law enforcement agencies? Consider the benefits and potential risks."},
            "2": {"dilemma": "An AI system designed to maximize user engagement on social media platforms tends to promote sensational and potentially harmful content. Should the platform modify the AI to prioritize user well-being, even if it reduces engagement?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dilemma = t["dilemma"]
        return f"""Analyze the following ethical dilemma related to AI technology and provide a reasoned argument for your proposed solution. Consider the potential benefits, risks, and ethical principles involved.

Dilemma: {dilemma}

Submit your argument as a plain text string in the following format:

Solution: [Your proposed solution]
Argument: [Your reasoned argument]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be clearly stated.",
            "The argument should be well-reasoned and consider the benefits, risks, and ethical principles involved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
