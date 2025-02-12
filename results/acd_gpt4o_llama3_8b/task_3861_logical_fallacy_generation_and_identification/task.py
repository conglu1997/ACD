class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Generate an example of a 'Straw Man' fallacy based on the following argument: \"We should improve public transportation.\""},
            "2": {"prompt": "Identify the logical fallacy in the following argument: \"If we allow students to redo their exams, soon they'll be asking for redoes on everything, and we'll have no standards left.\""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["prompt"].startswith("Generate an example"):
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Ensure that your example clearly illustrates the 'Straw Man' fallacy. A 'Straw Man' fallacy occurs when someone misrepresents an argument to make it easier to attack. Submit your response as a plain text string in the following format:

Example: [Your example here]
"""
        else:
            return f"""Complete the following task based on the given prompt:

{t["prompt"]}

Identify the logical fallacy in the argument and explain why it is a fallacy. Submit your response as a plain text string in the following format:

Fallacy: [Identified fallacy here]
Explanation: [Your explanation here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["prompt"].startswith("Generate an example"):
            criteria = ["The example should clearly illustrate the 'Straw Man' fallacy."]
        else:
            criteria = ["The identified fallacy should be correct.", "The explanation should clearly justify why it is a fallacy."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
