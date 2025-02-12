class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Your friend just lost their job and is feeling very down. They have been applying to new jobs but haven't had any luck yet. What advice would you give to support them in this difficult time?"},
            "2": {"scenario": "A colleague at work seems to be avoiding you after a recent argument. You value your professional relationship with them and want to resolve the issue. What advice would you give to address the situation and mend the relationship?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to read the following social scenario and provide empathetic advice to the person involved. Your advice should be supportive, considerate of their emotions, and practical in helping them navigate their situation.

Scenario: {t["scenario"]}

Instructions:
1. Understand the emotions and context of the given scenario.
2. Provide advice that addresses the emotional state and practical needs of the person involved.
3. Ensure your advice is empathetic, supportive, and constructive.

Your response should be in plain text format, structured as follows:

Advice: [Your empathetic advice]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The advice should be empathetic and considerate of the person's emotions.",
            "The advice should offer practical steps to help the person navigate their situation.",
            "The response should be supportive and constructive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
