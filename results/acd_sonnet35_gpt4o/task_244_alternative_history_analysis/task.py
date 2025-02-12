import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "event": "The invention of the printing press",
                "year": 1440,
                "change": "was delayed by 100 years"
            },
            {
                "event": "The American Revolution",
                "year": 1775,
                "change": "resulted in a negotiated compromise instead of independence"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Imagine an alternative history where {t['event']} in {t['year']} {t['change']}. Your task is to:

1. Briefly describe the original historical event and its significance (2-3 sentences).

2. Create an alternative narrative (200-250 words):
   a) Describe how the changed event unfolds.
   b) Explain the immediate consequences of this change.
   c) Explore the potential long-term effects on world history.

3. Analyze your alternative history (150-200 words):
   a) Identify at least two major areas (e.g., technology, politics, culture) that would be significantly affected.
   b) Explain how these changes might interact and create further consequences.
   c) Discuss any potential paradoxes or inconsistencies in your alternate timeline.

4. Compare and contrast (100-150 words):
   a) Compare your alternative history to our actual history.
   b) Identify any similarities or parallel developments that might occur despite the change.
   c) Explain why these similarities or parallels might exist.

5. Reflection (50-100 words):
   Discuss what this exercise reveals about the nature of historical causality and the role of key events in shaping history.

Ensure your response is creative yet historically plausible. Use your knowledge of history to make logical inferences about how changes would propagate through time."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections.",
            "The alternative narrative is creative yet historically plausible.",
            "The analysis demonstrates a deep understanding of historical cause-and-effect relationships.",
            "The comparison between alternative and actual history is insightful and well-reasoned.",
            "The reflection shows thoughtful consideration of historical causality and the significance of key events."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
