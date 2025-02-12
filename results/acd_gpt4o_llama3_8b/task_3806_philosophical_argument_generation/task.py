class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Is it possible to achieve true happiness? Discuss with reference to both utilitarian and deontological perspectives. Ensure that your argument considers potential objections and counters them."},
            "2": {"prompt": "Can machines ever possess consciousness? Discuss with reference to both functionalist and dualist perspectives. Ensure that your argument considers potential objections and counters them."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Based on the following prompt, generate a coherent and logical philosophical argument that reflects an understanding of relevant philosophical theories:\n\nPrompt:\n{prompt}\n\nProvide your response in the following format:\n\nArgument: [Your argument]\nExplanation: [A detailed explanation of the reasoning and philosophical theories behind your argument. Ensure that your explanation considers potential objections and counters them.]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The argument should be coherent and logical.", "The explanation should reflect an understanding of relevant philosophical theories.", "The explanation should address potential objections and counter them."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
