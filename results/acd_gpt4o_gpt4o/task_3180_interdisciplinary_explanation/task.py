class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Explain how the principles of thermodynamics apply to economic systems."
            },
            "2": {
                "concept": "Describe the relationship between quantum mechanics and computer science."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Your task is to explain the following concept in a clear and understandable manner: {t['concept']}\n"
            "Ensure that your explanation integrates knowledge from the relevant fields and presents the information coherently.\n"
            "Your explanation should cover the fundamental principles involved and how they interrelate across the disciplines.\n"
            "Provide your response in plain text format, structured as follows:\n"
            "Explanation: [Your explanation]"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
