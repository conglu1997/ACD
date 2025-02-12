class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept1": "Democracy", "concept2": "Monarchy"},
            "2": {"concept1": "Classical Music", "concept2": "Jazz"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compare and contrast the following two concepts, highlighting their similarities and differences:

Concept 1: {t['concept1']}
Concept 2: {t['concept2']}

Your response should include:
1. An introduction that briefly defines each concept.
2. A section on the similarities between the two concepts, with at least three distinct similarities.
3. A section on the differences between the two concepts, with at least three distinct differences.

Submit your response as a plain text string with clearly labeled sections for 'Introduction', 'Similarities', and 'Differences'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an introduction that briefly defines each concept.",
            "The response should include a section on the similarities between the two concepts, with at least three distinct similarities.",
            "The response should include a section on the differences between the two concepts, with at least three distinct differences."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
