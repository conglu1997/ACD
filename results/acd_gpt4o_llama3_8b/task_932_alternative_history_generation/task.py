class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The assassination of Archduke Franz Ferdinand in 1914.", "change": "The assassination attempt fails and the Archduke survives.", "actual_outcome": "The assassination led to the outbreak of World War I."},
            "2": {"event": "The signing of the Treaty of Versailles in 1919.", "change": "The treaty is never signed.", "actual_outcome": "The treaty imposed heavy reparations on Germany and contributed to the rise of Nazi Germany."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the given historical event and the actual outcome that resulted from it. Then, generate a plausible alternative historical scenario based on the provided change in that event. Your response should be detailed, logically consistent with the historical context, and between 150 to 300 words. Submit your response in the following format:

Event: {t['event']}
Change: {t['change']}
Actual Outcome: {t['actual_outcome']}

Alternative Scenario: [Your detailed alternative historical scenario]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The alternative scenario should be plausible, logically consistent with the historical context, and between 150 to 300 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
