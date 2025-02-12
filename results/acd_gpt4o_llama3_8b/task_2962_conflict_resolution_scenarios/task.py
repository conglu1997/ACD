class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Alice and Bob are colleagues working on a project. Alice feels that Bob isn't contributing enough, while Bob feels that Alice is micromanaging and not giving him enough space to work."
            },
            "2": {
                "scenario": "Emily and David are roommates. Emily likes to keep the place tidy, while David tends to be more relaxed about cleanliness. This has led to several arguments between them."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following conflict scenario and generate a dialogue or plan to resolve it. Your resolution should consider the perspectives of both parties and aim for a mutually beneficial outcome.

Scenario: {t['scenario']}

Your response should include:
1. A brief explanation of the conflict
2. A dialogue or plan to resolve the conflict

Submit your response as a plain text string in the following format:
Explanation: [Your explanation]
Resolution: [Your dialogue or plan]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should accurately summarize the conflict.",
            "The resolution should address the concerns of both parties and aim for a mutually beneficial outcome.",
            "The language used should be appropriate and empathetic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
