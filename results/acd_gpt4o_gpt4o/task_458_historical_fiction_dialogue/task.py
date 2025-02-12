class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"figures": ["Leonardo da Vinci", "Albert Einstein"], "context": "Discussing the future of science and technology."},
            "2": {"figures": ["Cleopatra", "Queen Victoria"], "context": "Discussing the role of women in leadership."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a fictional dialogue between the following two historical figures who never met in real life:

Figures: {t['figures'][0]} and {t['figures'][1]}

Context: {t['context']}

Ensure that the dialogue is creative, historically informed, and maintains consistent character traits and contexts. The dialogue should be at least 300 words long and should be written in plain text format. Follow this structure:

1. {t['figures'][0]}: [First line of dialogue]
2. {t['figures'][1]}: [Response]
3. Continue the dialogue in a similar format until the end.

Guidelines:
- Maintain the personality traits and historical context of each figure.
- Ensure the conversation flows naturally and is coherent.
- Incorporate historically accurate references and terminology where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The dialogue should be creative and historically informed.", "The dialogue should maintain consistent character traits and context.", "The dialogue should be at least 300 words long.", "The conversation should flow naturally and be coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
