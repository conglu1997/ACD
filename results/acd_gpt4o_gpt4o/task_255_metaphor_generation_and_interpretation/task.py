class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "time and river", "instruction": "Generate a metaphor that relates the concept of time to a river. Provide the metaphor in plain text format."},
            "2": {"metaphor": "Life is a journey, with its many paths and unknown destinations.", "instruction": "Interpret the provided metaphor. Explain its meaning and the imagery it evokes. Provide your interpretation in plain text format."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "topic" in t:
            instructions = f"""Your task is to generate a metaphor based on the following topics:

Topics: {t['topic']}

Ensure that the metaphor is creative and clearly relates the given concepts. Provide the metaphor in plain text format."""
        else:
            instructions = f"""Your task is to interpret the following metaphor:

Metaphor: {t['metaphor']}

Instruction: {t['instruction']}

Your interpretation should explain the meaning of the metaphor and the imagery it evokes. Provide your interpretation in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "topic" in t:
            criteria = [
                "The metaphor should creatively and clearly relate the given concepts.",
                "The metaphor should be coherent and meaningful."]
        else:
            criteria = [
                "The interpretation should accurately explain the meaning of the metaphor.",
                "The interpretation should discuss the imagery evoked by the metaphor."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
