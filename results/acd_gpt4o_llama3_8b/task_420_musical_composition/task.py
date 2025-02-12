class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "love", "constraints": "The composition should be in a major key and follow a simple AABA structure."},
            "2": {"theme": "adventure", "constraints": "The composition should be in a minor key and use a verse-chorus-verse-chorus structure."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a musical composition based on the following theme and constraints:

Theme: {t['theme']}
Constraints: {t['constraints']}

Ensure that the composition is coherent, adheres to the specified structure, and reflects the given theme. Provide the composition as a plain text string in the format of musical notation or chord progression. For example, you can use chord names (e.g., C, G, Am, F) or solfege syllables (e.g., do, re, mi, fa). Submit your composition as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The composition should be coherent and adhere to the specified structure.", "The composition should reflect the given theme.", "The composition should be provided in the format of musical notation or chord progression."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
