class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A genre characterized by complex rhythms, syncopation, and improvisation. Often features instruments like the saxophone, trumpet, and piano.", "expected_genre": "Jazz"},
            "2": {"theme": "A calm, serene night under the stars."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'description' in t:
            return f"""Identify the musical genre based on the following description: {t['description']} Submit your response as a plain text string."""
        else:
            return f"""Compose a short piece of music based on the following theme: {t['theme']} Submit your composition as a plain text string in the following format:

Composition:
[Your composition here]

Example:
Composition:
A gentle melody played on a piano, with soft, sustained notes to evoke the calmness of the night. The melody is simple, with a slow tempo and a repetitive structure to create a sense of peace and tranquility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'description' in t:
            criteria = [f"The response should identify the genre as {t['expected_genre']}."]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        else:
            return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
