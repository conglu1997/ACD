class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "happy", "constraints": "4/4 time signature, at least 8 measures, use at least 3 different pitches"},
            "2": {"sheet_music": "C D E F G A B C | C B A G F E D C"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            return f"""Your task is to generate a piece of music based on the given theme and constraints.

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure that your music is creative, follows the given constraints, and is notated correctly. Provide your response in the form of music notation (e.g., 'C D E F G A B C | C B A G F E D C')."""
        elif "sheet_music" in t:
            return f"""Your task is to analyze the provided piece of music and identify specific features.

Sheet Music: {t['sheet_music']}

Identify and explain the following features:
1. Key signature
2. Time signature
3. Melodic structure
Provide your analysis in plain text format."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theme" in t:
            criteria = [
                "The music should be creative and follow the given theme and constraints.",
                "The music notation should be correct and follow standard conventions."
            ]
        elif "sheet_music" in t:
            criteria = [
                "The analysis should accurately identify the key signature, time signature, and melodic structure.",
                "The explanations should be clear and logically sound."
            ]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
