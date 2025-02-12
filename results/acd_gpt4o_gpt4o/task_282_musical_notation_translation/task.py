class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "C D E F G A B C"},
            "2": {"notation": "E F G A B C D E"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following musical notation into plain text instructions. The notation represents a sequence of musical notes. Each note should be translated into its corresponding text representation in the order given. Here is the notation:

{t["notation"]}

Provide your response in plain text format. Each note should be separated by a space."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly translate the musical notation into plain text instructions.",
            "The notes should be in the correct order as given in the notation.",
            "Each note should be separated by a space."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
