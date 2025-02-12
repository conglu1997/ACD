class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"issue": "The computer won't turn on. The power light is off and there are no sounds or lights coming from the computer."},
            "2": {"issue": "The computer is running very slow. It takes a long time to open applications and the system often freezes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        issue = t["issue"]
        instructions = f"""Your task is to provide a step-by-step troubleshooting procedure to resolve the following computer issue:

Issue: {issue}

Ensure your troubleshooting steps are clear, logical, and include all necessary details. Consider common causes and provide potential solutions for each step. The procedure should be comprehensive and cover both identification and resolution of potential causes. 

Provide your response in the following format:

Step 1: [Description of step]
Step 2: [Description of step]
...
Step N: [Description of step]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The troubleshooting steps should be clear and logical.",
            "The procedure should be comprehensive and cover common causes of the issue.",
            "Each step should be detailed and provide potential solutions.",
            "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
