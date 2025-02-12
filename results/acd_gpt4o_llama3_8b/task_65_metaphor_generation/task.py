class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source": "time", "target": "river"},
            "2": {"source": "knowledge", "target": "light"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        source = t["source"]
        target = t["target"]
        return f"""Generate a metaphor that connects the concept of '{source}' to the concept of '{target}'. The metaphor should be creative, meaningful, and clearly illustrate the relationship between the two concepts. Submit your metaphor as a plain text string in a single sentence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The metaphor should be creative.",
            "The metaphor should clearly illustrate the relationship between the two concepts.",
            "The metaphor should be meaningful and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
