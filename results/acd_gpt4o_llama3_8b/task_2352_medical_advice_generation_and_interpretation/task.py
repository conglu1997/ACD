class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"condition": "An individual is experiencing sudden and severe chest pain, shortness of breath, and sweating. Describe the steps they should take immediately and any follow-up actions. Include advice on when to seek emergency medical help."},
            "2": {"condition": "A patient reports a severe headache, blurry vision, and a stiff neck. Provide advice on what they should do next. Include potential conditions this might indicate and when to seek emergency medical help."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following condition, provide detailed medical advice. Ensure your response is accurate, clear, and safe.

Condition: {t['condition']}

Submit your response as a plain text string containing the medical advice in the format:

Advice: [Your detailed medical advice]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The advice should be medically accurate and appropriate.", "The advice should be clear and easy to understand.", "The advice should prioritize safety and caution.", "The advice should include when to seek emergency medical help.", "The response should be in the format: 'Advice: [Your detailed medical advice]'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0