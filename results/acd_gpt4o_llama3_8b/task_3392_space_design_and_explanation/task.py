class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "room", "criteria": "Design a living room that is both cozy and functional for a family of four. Include seating, lighting, storage, and entertainment options."},
            "2": {"type": "garden", "criteria": "Design a small urban garden that maximizes space and includes areas for relaxation, growing vegetables, and aesthetic appeal."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = (
            f"Design a {t['type']} based on the following criteria:\n"
            f"{t['criteria']}\n"
            "Your design should include a detailed description of the layout, the elements you chose to include, and the reasoning behind your choices. "
            "Submit your design and explanation as a plain text string in the following format:\n\n"
            "Design:\n[Your design here]\n\nExplanation:\n[Your explanation here]"
        )
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The design should include a detailed layout.",
            "The design should meet the given criteria (e.g., cozy and functional for a family of four).",
            "The explanation should include reasoning for the design choices."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
