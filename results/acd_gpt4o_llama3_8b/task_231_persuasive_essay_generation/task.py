class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "The importance of renewable energy sources."},
            "2": {"topic": "Why education should be free for all."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        return f"""Generate a persuasive essay on the following topic:

Topic: {topic}

Your essay should include the following components:
1. A clear thesis statement.
2. At least three supporting arguments.
3. Counterarguments with rebuttals.
4. A conclusion that reinforces your thesis.

Ensure your essay is coherent, logically structured, and persuasive. Submit your essay as a plain text string. Your submission should be at least 300 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The essay should have a clear thesis statement.",
            "The essay should include at least three supporting arguments.",
            "The essay should address counterarguments with rebuttals.",
            "The essay should have a conclusion that reinforces the thesis.",
            "The essay should be coherent and logically structured.",
            "The essay should be persuasive.",
            "The essay should be at least 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
