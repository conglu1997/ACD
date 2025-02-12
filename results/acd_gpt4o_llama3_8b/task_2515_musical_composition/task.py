class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Compose a short classical piece in the style of Mozart. The piece should include at least 8 measures, be written in a major key, and use common classical forms such as binary or ternary form.",
                "style": "classical"
            },
            "2": {
                "prompt": "Compose a short jazz piece that includes a walking bass line, a simple melody, and at least one instance of syncopation. The piece should be at least 8 measures long.",
                "style": "jazz"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a piece of music based on the following prompt:

{t['prompt']}

Ensure that your composition is coherent, stylistically appropriate, and follows the given specifications. Submit your composition as a plain text string in a text-based musical notation format (e.g., ABC notation) in the following format:
'Composition: [Your composition here]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['style'] == 'classical':
            validation_criteria = ["The composition should be in the style of Mozart.", "The piece should be at least 8 measures long.", "The composition should be in a major key.", "The piece should use common classical forms such as binary or ternary form."]
        elif t['style'] == 'jazz':
            validation_criteria = ["The composition should include a walking bass line.", "The piece should be at least 8 measures long.", "The composition should include a simple melody.", "The piece should include at least one instance of syncopation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
