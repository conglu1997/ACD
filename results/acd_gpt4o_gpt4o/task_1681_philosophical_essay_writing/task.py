class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Write an essay on the concept of free will and determinism.", "type": "philosophical_essay"},
            "2": {"task": "Construct an argument either in favor of or against the idea that 'The unexamined life is not worth living.'", "type": "philosophical_argument"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'philosophical_essay':
            return f"""Your task is to write an essay on the concept of free will and determinism. Discuss the various perspectives on this topic, including both philosophical and practical implications. Ensure that your essay is logically coherent, demonstrates depth of thought, and is creatively presented. Provide your response in plain text format."""
        elif t['type'] == 'philosophical_argument':
            return f"""Your task is to construct an argument either in favor of or against the idea that 'The unexamined life is not worth living.' Present your argument clearly, ensuring it is logically valid, demonstrates depth of thought, and is creatively presented. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The content should demonstrate logical coherence.", "The submission should show depth of thought and creativity."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
