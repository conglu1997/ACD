class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": "All humans are mortal. Socrates is a human.", "conclusion": "Socrates is mortal."},
            "2": {"argument": "All cats are mammals. All mammals have fur. Therefore, all cats have fur."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "premises" in t:
            return f"""Your task is to generate a formal logical argument based on the given premises and conclusion.

Premises: {t['premises']}

Conclusion: {t['conclusion']}

Ensure that your argument is logically valid and follows a clear, formal structure. Provide your argument in the following format:

Premises:
- [Premise 1]
- [Premise 2]
...

Conclusion:
- [Conclusion]"""
        elif "argument" in t:
            return f"""Your task is to analyze the provided logical argument for validity.

Argument: {t['argument']}

Determine whether the argument is logically valid and explain your reasoning. Provide your analysis in the following format:

Validity:
- [Is the argument valid? Yes/No]

Reasoning:
- [Explanation of your reasoning]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "premises" in t:
            criteria = [
                "The argument should be logically valid based on the given premises and conclusion.",
                "The argument should follow a clear, formal structure."
            ]
        elif "argument" in t:
            criteria = [
                "The analysis should accurately determine the validity of the provided argument.",
                "The reasoning should be clearly explained and logically sound."
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
