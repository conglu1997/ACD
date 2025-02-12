class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The signing of the Treaty of Versailles in 1919"},
            "2": {"hypothetical_change": "What if the Roman Empire had never fallen?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'event' in t:
            return f"""Your task is to analyze the following historical event:

Event: {t['event']}

Provide a detailed analysis of the event, including its causes, key players, and consequences. Discuss the historical significance of the event and its impact on subsequent history. Ensure your analysis is well-researched, coherent, and includes accurate historical facts. Provide your analysis in plain text format without additional formatting."""
        else:
            return f"""Your task is to generate a plausible hypothesis based on the following hypothetical change in history:

Hypothetical Change: {t['hypothetical_change']}

Provide a detailed hypothesis that explores how history might have unfolded differently if this change had occurred. Discuss the potential impacts on political, social, and economic structures, as well as any significant events that might have been altered. Ensure your hypothesis is logical, coherent, and grounded in historical knowledge. Provide your hypothesis in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'event' in t:
            criteria = ["The analysis should be detailed.", "The analysis should include causes, key players, and consequences of the event.", "The analysis should discuss the historical significance of the event.", "The analysis should be well-researched and coherent.", "The analysis should include accurate historical facts."]
        else:
            criteria = ["The hypothesis should be detailed.", "The hypothesis should explore the potential impacts of the hypothetical change.", "The hypothesis should be logical and coherent.", "The hypothesis should be grounded in historical knowledge."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
