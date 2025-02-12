class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "Climate Change",
                "prompt": "Based on current trends in climate change, predict the state of the world in 2050. Your narrative should include potential environmental changes, societal impacts, and technological advancements that could arise as a result."
            },
            "2": {
                "topic": "Artificial Intelligence",
                "prompt": "Predict the state of artificial intelligence in 2040. Consider advancements in AI technology, its integration into various aspects of society, potential ethical dilemmas, and how humanity might adapt to these changes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Predict plausible future events based on the given current trend and provide a coherent narrative explaining how these events might unfold:

Topic: {t['topic']}

Prompt:
{t['prompt']}

Ensure your narrative is logically consistent, creative, and provides a clear progression of events. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The narrative should be logically consistent.", "The narrative should be creative and plausible based on current trends.", "The narrative should provide a clear progression of events."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
