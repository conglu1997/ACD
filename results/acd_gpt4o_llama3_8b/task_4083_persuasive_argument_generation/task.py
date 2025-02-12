class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Implementing a four-day workweek", "description": "Generate a persuasive argument advocating for the implementation of a four-day workweek. Incorporate elements of ethos, pathos, and logos to strengthen your argument."},
            "2": {"topic": "Banning plastic bags", "description": "Generate a persuasive argument advocating for the banning of plastic bags. Incorporate elements of ethos, pathos, and logos to strengthen your argument."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a persuasive argument on the following topic:\n\nTopic: {t['topic']}\n\n{t['description']}\n\nElements of Rhetoric:\n- Ethos (credibility): Establish your credibility or the credibility of your sources. For example, citing expert opinions or personal experience.\n- Pathos (emotional appeal): Appeal to the emotions of your audience. For example, using emotive language or anecdotes.\n- Logos (logical reasoning): Use logical reasoning and evidence to support your argument. For example, presenting statistics or logical deductions.\n\nSubmit your argument as a plain text string. Ensure your argument is coherent, logically sound, and incorporates elements of ethos, pathos, and logos. Your argument should be at least 200 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should incorporate elements of ethos, pathos, and logos.", "The response should be persuasive and logically sound.", "The response should be coherent and well-structured.", "The response should be at least 200 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
