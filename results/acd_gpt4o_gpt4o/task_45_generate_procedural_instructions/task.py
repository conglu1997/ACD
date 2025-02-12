class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "How to bake a chocolate cake.", "requirements": "Include ingredients, preparation steps, baking time, and temperature."},
            "2": {"task": "How to change a flat tire on a car.", "requirements": "Include necessary tools, safety precautions, and step-by-step procedure."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        task = t["task"]
        requirements = t["requirements"]
        instructions = f"""Your task is to generate detailed step-by-step instructions for the following process:

{task}

Ensure that your instructions are clear, logically ordered, and cover all necessary steps to complete the task. Specifically, your instructions should meet the following requirements:
{requirements}

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The instructions should be clear and easy to follow.",
            "The instructions should be logically ordered.",
            "The instructions should cover all necessary steps to complete the task."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
