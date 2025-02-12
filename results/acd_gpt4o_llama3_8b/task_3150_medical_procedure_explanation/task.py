class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "procedure": "Cardiopulmonary Resuscitation (CPR)",
                "situation": "An adult suddenly collapses and is unresponsive in a public park with bystanders present."
            },
            "2": {
                "procedure": "Appendectomy",
                "situation": "A 25-year-old patient is diagnosed with acute appendicitis and is experiencing severe lower right abdominal pain, nausea, and fever."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Describe the step-by-step process for the given medical procedure: {t['procedure']} in the context of the provided situation: {t['situation']}.

2. Explain the rationale behind each step, including the underlying medical principles and the importance of each action. Ensure that each step aligns with standard medical practices.

Submit your response as a plain text string in the following format:

Procedure Description:
[Step-by-step description]

Rationale Explanation:
[Explanation of the rationale behind each step]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The procedure description should be accurate, detailed, and cover all critical steps.",
            "The rationale explanation should be clear, logical, and include the underlying medical principles and importance of each step.",
            "Each step in the procedure should align with standard medical practices.",
            "The submission should be well-organized and clearly written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
