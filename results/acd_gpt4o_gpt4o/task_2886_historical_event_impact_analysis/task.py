class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The Industrial Revolution", "focus": "Analyze how the Industrial Revolution impacted urbanization, labor, and economic structures in Europe. Include specific examples and long-term consequences."},
            "2": {"event": "World War II", "focus": "Discuss the global political changes that occurred as a result of World War II, particularly the emergence of the United States and the Soviet Union as superpowers. Include specific events and policies that shaped these changes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the impact of the following historical event on society, culture, and global developments. Provide a detailed analysis that addresses the specified focus area.

Event: {t['event']}
Focus: {t['focus']}

Your analysis should be well-organized, coherent, and demonstrate a deep understanding of the historical context and its long-term consequences. Your response should be between 300 and 500 words. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should be well-organized and coherent.", "The analysis should demonstrate a deep understanding of the historical context.", "The analysis should address the specified focus area and discuss long-term consequences.", "The response should be between 300 and 500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
