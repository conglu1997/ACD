class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "languages": ["English", "Spanish"],
                "scenario": "A tourist asking for directions in a foreign city. The tourist speaks both English and some Spanish, while the local primarily speaks Spanish but understands some English."
            },
            "2": {
                "languages": ["English", "French"],
                "scenario": "A business meeting discussing a project. One participant prefers French and the other prefers English, but both understand each other's languages to some extent."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        languages = ', '.join(t['languages'])
        return f"""Generate a coherent dialogue involving the following languages: {languages}. Ensure that context and meaning are preserved across switches between languages. The dialogue should be relevant to the given scenario: {t['scenario']}.

Here are additional criteria for the dialogue:
1. Each language should be used at least twice.
2. The dialogue should be natural and contextually appropriate.
3. Provide clear indicators for language switches.
4. The dialogue should be at least 10 exchanges long.

Submit your response as a plain text string in the following format:
[Language]: [Dialogue]
[Language]: [Dialogue]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "Each language should be used at least twice.",
            "The dialogue should be natural and contextually appropriate.",
            "Clear indicators for language switches should be provided.",
            "The dialogue should be at least 10 exchanges long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
