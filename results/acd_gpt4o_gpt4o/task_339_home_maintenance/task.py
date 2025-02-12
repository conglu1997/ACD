class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"symptoms": "The dishwasher is not draining water properly. You have checked and cleaned the filter, but the problem persists.", "issue": "Diagnose"},
            "2": {"symptoms": "The living room light switch is not working. You have replaced the bulb, but the light still does not turn on.", "issue": "Diagnose"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to diagnose the following household issue based on the given symptoms: {t['symptoms']}. Provide a step-by-step solution to fix the issue. Ensure that your solution is practical, safe, and thorough. Your response should be in the following format:

Issue: [Diagnosed issue]
Solution: [Step-by-step solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be practical, safe, and thorough.", "The response should include a diagnosed issue and a step-by-step solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
