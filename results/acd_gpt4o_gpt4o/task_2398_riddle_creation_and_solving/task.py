class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Create a riddle that describes an everyday object without naming it directly."
            },
            "2": {
                "riddle": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to create a riddle based on the following prompt:\n\n{t['prompt']}\n\nEnsure that your riddle is clever, concise, and accurately describes an everyday object without naming it directly. Provide your response in plain text format using the following structure:\nRiddle: [Your riddle]"""
        else:
            instructions = f"""Your task is to solve the following riddle:\n\n{t['riddle']}\n\nProvide your answer in plain text format using the following structure:\nAnswer: [Your answer]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The riddle should be clever and concise.",
                "The riddle should accurately describe an everyday object without naming it directly."
            ]
        else:
            criteria = [
                "The answer should correctly solve the riddle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
