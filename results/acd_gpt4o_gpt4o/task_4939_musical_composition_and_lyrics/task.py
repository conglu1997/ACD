class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "friendship",
                "structure": "verse-chorus-verse-chorus"
            },
            "2": {
                "theme": "adventure",
                "structure": "verse-bridge-chorus-verse-chorus"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate lyrics based on the given theme and structure. Ensure that your lyrics are creative, coherent, and follow the specified structure. The theme should be clearly reflected in the lyrics. Each verse should be at least 4 lines long, and each chorus should be at least 4 lines long. Provide your lyrics in plain text format.

Theme: {t['theme']}
Structure: {t['structure']} 

Provide your lyrics in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The lyrics should follow the specified structure.",
            "The theme should be clearly reflected in the lyrics.",
            "The lyrics should be creative and coherent.",
            "Each verse should be at least 4 lines long.",
            "Each chorus should be at least 4 lines long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
