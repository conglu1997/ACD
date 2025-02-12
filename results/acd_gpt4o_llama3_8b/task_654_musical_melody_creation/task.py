class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scale": "C Major", "length": 8},
            "2": {"scale": "A Minor", "length": 12}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a melody using the {t['scale']} scale with a length of {t['length']} notes. Each note should be represented by its letter name (e.g., C, D, E, F, G, A, B) and separated by spaces. After creating the melody, explain the musical theory behind it, including the choice of notes and any patterns or motifs used. Submit your melody in a simple text format followed by the explanation as a plain text string in the format:

Melody: [your melody]
Explanation: [your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The melody should use only notes from the given scale.", f"The melody should be exactly {t['length']} notes long.", "The explanation should be coherent and accurately describe the choice of notes and any patterns or motifs used.", "The response format should include 'Melody:' followed by the melody and 'Explanation:' followed by the explanation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
