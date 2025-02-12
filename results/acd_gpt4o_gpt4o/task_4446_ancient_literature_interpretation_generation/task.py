class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"excerpt": "Sing, O goddess, the anger of Achilles son of Peleus, that brought ill to the Achaeans."},
            "2": {"prompt": "Write a short poem inspired by the themes and style of Homer's Iliad."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "excerpt" in t:
            return f"""Interpret the following excerpt from ancient literature. Provide a detailed analysis of its meaning, themes, and historical context:

{t['excerpt']}

Your response should be in plain text format and well-structured."""
        elif "prompt" in t:
            return f"""Write a short poem inspired by the themes and style of Homer's Iliad. Ensure your poem reflects the epic nature of the original work and captures its key themes.

Provide your poem in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []

        if "excerpt" in t:
            criteria.append("The response should provide a detailed analysis of the excerpt's meaning, themes, and historical context.")
        elif "prompt" in t:
            criteria.append("The poem should reflect the epic nature of the Iliad and capture its key themes.")

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0