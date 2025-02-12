class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "A formal business meeting between a manager and an employee discussing a project update.",
                "transformation": "Rewrite the dialogue in an informal setting, such as a casual conversation between friends."
            },
            "2": {
                "context": "A doctor explaining a medical condition to a patient in a professional manner.",
                "transformation": "Rewrite the dialogue as a friendly conversation between a doctor and a close relative."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Task 1: Generate a dialogue based on the following context: {t['context']}.

Task 2: Transform the generated dialogue according to the specified transformation: {t['transformation']}.

Submit your responses in the following format:

1. Original Dialogue:
[Your generated dialogue here]

2. Transformed Dialogue:
[Your transformed dialogue here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The original dialogue should be coherent, contextually appropriate, and reflect the given context.",
            "The transformed dialogue should accurately reflect the new context while maintaining the essence of the original conversation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
