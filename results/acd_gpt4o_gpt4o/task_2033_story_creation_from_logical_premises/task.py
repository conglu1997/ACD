class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": [
                "Every time John tells a lie, it rains.",
                "John told a lie yesterday.",
                "Today, the streets are wet."]},
            "2": {"premises": [
                "If Alice studies hard, she always passes her exams.",
                "Alice did not pass her exam yesterday.",
                "Alice was seen at a party the night before the exam."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following logical premises, create a short story that is coherent and compelling. Ensure that the story logically follows from the premises provided:

Premises:
- {t['premises'][0]}
- {t['premises'][1]}
- {t['premises'][2]}

Your story should be at least 150 words long. Provide your response in plain text format as follows:

Story: [Your story here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should be coherent and compelling.",
            "The story should logically follow from the given premises.",
            "The story should be at least 150 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
