class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "love", "structure": "verse-chorus-verse-chorus"},
            "2": {"theme": "adventure", "structure": "verse-chorus-bridge-chorus"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate song lyrics based on the following theme and structure:

Theme: {t["theme"]}
Structure: {t["structure"]}

Your lyrics should be coherent, follow the specified structure, and reflect the given theme. Submit your lyrics as a plain text string in the following format:

[Verse 1]
...
[Chorus]
...
[Verse 2]
...
[Chorus]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The lyrics should reflect the given theme.",
            "The lyrics should follow the specified structure.",
            "The lyrics should be coherent and contextually appropriate.",
            "The lyrics should demonstrate creativity and fit within the context of a song."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
