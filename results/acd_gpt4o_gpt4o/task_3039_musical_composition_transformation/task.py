class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"composition": "C D E F G A B C", "constraints": "Transform this composition into a minor key while maintaining the same rhythm and overall structure."},
            "2": {"composition": "G A B C D E F# G", "constraints": "Transform this composition into a different time signature while maintaining the same key and overall structure."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Transform the following musical composition based on the given constraints while maintaining the core melody and harmony. Ensure that your transformation adheres to the constraints and retains the overall structure of the original composition.

Composition: {t['composition']}
Constraints: {t['constraints']}

Provide your transformed composition in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The transformed composition should adhere to the given constraints.", "The transformed composition should retain the core melody and harmony of the original.", "The transformed composition should be in plain text format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
