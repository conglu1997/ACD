class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "The benefits of renewable energy sources over fossil fuels."},
            "2": {"topic": "The necessity of implementing stricter gun control laws."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        instructions = f"""Your task is to write a persuasive essay on the following topic:

{topic}

Your essay should present a clear argument and support it with evidence. It should be well-structured with an introduction, body paragraphs, and a conclusion. The essay should be between 300 and 500 words long. Ensure that your writing is persuasive, logically ordered, and uses appropriate rhetorical devices.

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The essay should present a clear argument.",
            "The argument should be supported with evidence.",
            "The essay should be well-structured with an introduction, body paragraphs, and a conclusion.",
            "The writing should be persuasive and logically ordered."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
