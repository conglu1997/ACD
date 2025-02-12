class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "expression": "😊"
            },
            "2": {
                "expression": "😔"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to interpret the given facial expression and generate an appropriate response to the identified emotion or state.

Facial Expression: {t['expression']}

Submit your response in the following format:

Emotion: [Identified emotion]
Response: [Your appropriate response]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly identify the emotion conveyed by the facial expression.",
            "The response should be appropriate, coherent, and empathetic given the identified emotion."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
