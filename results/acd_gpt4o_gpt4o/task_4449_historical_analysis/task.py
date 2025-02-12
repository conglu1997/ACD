class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Berlin Wall in 1989", "prompt": "Analyze the political, social, and economic impacts of the fall of the Berlin Wall. Discuss how it contributed to the end of the Cold War."},
            "2": {"figure": "Cleopatra VII", "prompt": "Discuss the political strategies and significance of Cleopatra VII's reign in ancient Egypt. Analyze how her relationships with Julius Caesar and Mark Antony influenced Roman politics."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "event" in t:
            instructions = f"""Your task is to analyze the historical event described below and write an interpretive essay on it.

Event: {t['event']}

Prompt: {t['prompt']}

Ensure that your essay includes accurate historical information, a clear analysis of the impacts, and a well-structured argument. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to analyze the historical figure described below and write an interpretive essay on them.

Figure: {t['figure']}

Prompt: {t['prompt']}

Ensure that your essay includes accurate historical information, a clear analysis of the figure's significance, and a well-structured argument. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The essay should include accurate historical information.", "The essay should provide a clear analysis of the impacts or significance.", "The essay should be well-structured and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
