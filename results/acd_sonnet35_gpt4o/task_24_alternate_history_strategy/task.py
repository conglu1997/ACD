import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'event': 'World War II',
                'change': 'Germany develops nuclear weapons before the United States',
                'year': 1944
            },
            {
                'event': 'American Revolution',
                'change': 'France decides not to support the American colonies',
                'year': 1777
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reimagine the course of {t['event']} with the following significant change: {t['change']}. The year is now {t['year']}.

1. Briefly describe how events might have unfolded differently up to this point (2-3 sentences).
2. Assuming you are a strategic advisor to the side most negatively impacted by this change, develop a strategic plan to turn the tide in their favor. Your plan should include:
   a) Three main objectives (1 sentence each)
   b) Two potential obstacles and how to overcome them (1-2 sentences each)
   c) One innovative or unexpected tactic that could provide a significant advantage (2-3 sentences)
3. Explain how your strategy takes into account the historical, technological, and geopolitical realities of the time, as well as the implications of the changed event (2-3 sentences).

Ensure your response is historically plausible, strategically sound, and creative in its approach to the altered scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a strong understanding of the historical event and its context.",
            "The alternative history scenario is plausible and logically consistent with the given change.",
            "The strategic plan is well-thought-out, addressing multiple aspects of the situation.",
            "The plan takes into account historical, technological, and geopolitical realities of the time.",
            "The response shows creativity and critical thinking in developing an innovative tactic.",
            "The explanation of how the strategy accounts for the changed event is clear and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
