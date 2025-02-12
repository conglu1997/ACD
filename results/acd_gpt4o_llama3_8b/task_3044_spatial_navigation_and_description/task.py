class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"environment": "You are in a city park with four landmarks: a fountain, a playground, a cafe, and an exit. The fountain is at the center, the playground is to the north, the cafe is to the east, and the exit is to the south. Describe the route from the playground to the cafe.", "start": "playground", "end": "cafe"},
            "2": {"environment": "You are inside a large library with three sections: Fiction, Non-Fiction, and Reference. The Fiction section is to the west, the Non-Fiction section is to the east, and the Reference section is to the north. Describe the route from the entrance to the Reference section.", "start": "entrance", "end": "Reference section"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following environment description, describe the step-by-step route from {t['start']} to {t['end']}.

Environment: {t['environment']}

Ensure that your description is clear, detailed, and follows a logical sequence. Submit your description as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description must be clear and detailed.",
            "The route must be logically correct based on the environment description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
