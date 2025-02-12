class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A programmer who accidentally deletes the entire codebase on a Friday evening. The team is preparing for a major release on Monday, and everyone is working remotely."},
            "2": {"scenario": "A cat that somehow manages to always land on its feet, even in the most ridiculous situations. The cat has become an internet sensation, and people are sharing videos of its antics."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a humorous joke based on the following scenario: '{t["scenario"]}'. The joke should be original, contextually appropriate, and should make sense within the given scenario. Ensure that the humor is lighthearted and non-offensive. Examples of what is not considered humorous or appropriate include jokes that are offensive, discriminatory, or insensitive. Submit your joke as a single sentence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The joke should be humorous.",
            "The joke should be original and not a well-known joke.",
            "The joke should be contextually appropriate.",
            "The joke should be submitted as a single sentence.",
            "The joke should be lighthearted and non-offensive."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
