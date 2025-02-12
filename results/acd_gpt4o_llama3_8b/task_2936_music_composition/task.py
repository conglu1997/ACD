class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "A journey through space",
                "constraints": "The composition should include at least three distinct sections, each representing different stages of the journey. Use descriptive language and imagery to convey the vastness and mystery of space."
            },
            "2": {
                "theme": "A summer day at the beach",
                "constraints": "Write song lyrics that capture the essence of a summer day at the beach. Include references to the sun, sand, sea, and any activities or feelings associated with this setting. The lyrics should be at least 16 lines long and should rhyme."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with creating a musical composition or writing song lyrics based on the given theme and constraints. Ensure that your composition or lyrics are coherent, engaging, and adhere to the provided constraints.

Theme: {t['theme']}
Constraints: {t['constraints']}

Submit your composition or lyrics in the following format:
1. Composition/Lyrics: [Your composition or lyrics]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition or lyrics should adhere to the given theme.",
            "The submission should meet all the specified constraints.",
            "The composition or lyrics should be coherent and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
