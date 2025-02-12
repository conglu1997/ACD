class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "premises": [
                    "If it rains, the ground will be wet.",
                    "It is raining."
                ],
                "conclusion": "The ground is wet."
            },
            "2": {
                "premises": [
                    "All humans are mortal.",
                    "Socrates is a human."
                ],
                "conclusion": "Socrates is mortal."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following premises, generate a logical conclusion and evaluate the validity of the argument:

Premises:
{chr(10).join(t['premises'])}

Conclusion: {t['conclusion']}

Ensure that the conclusion logically follows from the premises, and clearly state whether the argument is valid or invalid. Submit your evaluation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should correctly identify whether the argument is valid or invalid based on the given premises.",
            "The response should provide a clear and logical explanation of the evaluation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
