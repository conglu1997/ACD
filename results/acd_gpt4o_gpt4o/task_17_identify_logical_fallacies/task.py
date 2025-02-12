class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"argument": "If we don't increase the budget for education, our children will fail in life. Therefore, we must increase the budget for education."},
            "2": {"argument": "Either we ban all cars to stop pollution, or our planet will be destroyed. We don't want our planet to be destroyed, so we must ban all cars."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        argument = t["argument"]
        instructions = f"""Your task is to identify and correct the logical fallacy in the following argument:

{argument}

Provide your response in the following format:

Logical Fallacy: [Name the logical fallacy]
Corrected Argument: [Provide the corrected argument without the logical fallacy]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify the logical fallacy.",
            "The response should provide an argument without the logical fallacy.",
            "The corrected argument should be logically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
