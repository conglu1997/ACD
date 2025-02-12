class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sequence": [1, 4, 9, 16]},
            "2": {"sequence": [2, 4, 8, 16, 32]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to predict the next two elements in the following temporal sequence:

{t['sequence']}

Provide your predictions in plain text format as follows:

Prediction 1: [Your first prediction]
Prediction 2: [Your second prediction]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['sequence'] == [1, 4, 9, 16]:
            criteria = ["The response should predict the next two elements as 25 and 36."]
        elif t['sequence'] == [2, 4, 8, 16, 32]:
            criteria = ["The response should predict the next two elements as 64 and 128."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
