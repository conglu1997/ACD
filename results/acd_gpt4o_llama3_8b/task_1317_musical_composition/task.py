class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"style": "classical", "structure": "sonata", "key": "C major", "length": "1 minute"},
            "2": {"style": "jazz", "structure": "blues", "key": "F minor", "length": "1 minute"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a musical piece in the {t['style']} style, following the {t['structure']} structure, and in the key of {t['key']}. The piece should be approximately {t['length']} in duration. Ensure that your composition is coherent, follows the specified musical form, and adheres to the given key. Submit your composition as a plain text string representing the musical notation or a detailed description of the piece.

Example Format:
Title: [Your Title]
Musical Notation or Description: [Your musical notation or a detailed description of the composition]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should follow the specified musical style.",
            "The composition should adhere to the given structure.",
            "The composition should be in the indicated key.",
            "The composition should be coherent and musically sound.",
            "The composition should be approximately the specified length."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
