class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The French Revolution", "focus": "causes and outcomes", "word_count": 500},
            "2": {"event": "The Industrial Revolution", "focus": "impact on society", "word_count": 500}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze and interpret the following historical event based on the given focus. Write an insightful essay that covers the specified aspects in approximately {t['word_count']} words.

Event: {t['event']}
Focus: {t['focus']}

Ensure that your essay includes:

1. An introduction that provides context for the event.
2. A detailed analysis of the specified focus.
3. Relevant historical facts and interpretations.
4. A conclusion that summarizes your analysis.

Your essay should be well-structured, informative, and demonstrate a deep understanding of the historical event."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The essay should include an introduction, detailed analysis, relevant historical facts, and a conclusion.",
                    "The analysis should be insightful and demonstrate a deep understanding of the event.",
                    "The essay should be well-structured and approximately the specified word count."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
