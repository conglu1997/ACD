class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A friend looks at you and raises an eyebrow while you discuss your weekend plans."},
            "2": {"scenario": "During a meeting, a colleague crosses their arms, leans back in their chair, and avoids eye contact."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Interpret the following non-verbal communication cue and explain what it might signify. Additionally, generate a similar non-verbal cue for a different context and describe the context and the cue in detail.\n\nScenario: {scenario}\n\nYour response should include:\n1. Interpretation: [Your interpretation of the given scenario]\n2. Generated Cue: [Your generated non-verbal cue]\n3. Context: [The context for your generated cue]\n\nEnsure that your interpretation and generated cue are clear, contextually appropriate, and demonstrate an understanding of non-verbal communication."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The interpretation should be plausible and contextually appropriate.", "The generated cue should be clear, contextually fitting, and demonstrate an understanding of non-verbal communication."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
