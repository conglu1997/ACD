class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "generation",
                "major_premise": "All humans are mortal.",
                "minor_premise": "Socrates is a human."
            },
            "2": {
                "task_type": "verification",
                "syllogism": "All birds can fly. Penguins are birds. Therefore, penguins can fly."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generation':
            return f"""Generate a valid conclusion for the following syllogism:

Major Premise: {t['major_premise']}
Minor Premise: {t['minor_premise']}

Submit your conclusion as a plain text string."""
        elif t['task_type'] == 'verification':
            return f"""Verify the validity of the following syllogism:

{t['syllogism']}

Indicate whether the syllogism is valid or invalid and explain your reasoning. Submit your answer as a plain text string in the format: 'Validity: [valid/invalid]. Reasoning: [Your reasoning].'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generation':
            criteria = [
                "The conclusion should logically follow from the premises.",
                "The conclusion should not introduce new terms.",
                "The conclusion should be a plain text string."
            ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        elif t['task_type'] == 'verification':
            criteria = [
                "The validity judgment should be correct.",
                "The reasoning should explain why the syllogism is valid or invalid.",
                "The submission should follow the specified format."
            ]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
