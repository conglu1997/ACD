class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"characters": ["Albert Einstein", "Sherlock Holmes"], "scenario": "discussing quantum mechanics in a modern-day coffee shop"},
            "2": {"characters": ["Cleopatra", "Wonder Woman"], "scenario": "debating leadership strategies in an intergalactic council meeting"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a plausible dialogue between the following characters in the given scenario:

Characters: {', '.join(t['characters'])}
Scenario: {t['scenario']}

Ensure that the dialogue captures the unique personalities and attributes of each character, and is engaging, coherent, and contextually appropriate. The dialogue should be at least 15 exchanges long (one exchange being a back-and-forth between the two characters).

Provide your response in plain text format using the following structure:

[Character 1]: [Dialogue]
[Character 2]: [Dialogue]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be at least 15 exchanges long.",
            "The dialogue should capture the unique personalities and attributes of each character.",
            "The dialogue should be engaging, coherent, and contextually appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
