class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event1": "The Industrial Revolution in Britain (1760-1840)",
                "event2": "The Digital Revolution (late 20th to early 21st century)",
                "task": "Compare and contrast the Industrial Revolution in Britain with the Digital Revolution. Identify key similarities and differences in their causes, effects on society, and long-term impacts."
            },
            "2": {
                "event1": "The French Revolution (1789-1799)",
                "event2": "The Russian Revolution (1917)",
                "task": "Compare and contrast the French Revolution with the Russian Revolution. Discuss the social, political, and economic causes of each revolution, as well as their outcomes and historical significance."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given events:

Event 1: {t['event1']}
Event 2: {t['event2']}

Your task is to {t['task']}.

In your analysis, ensure that you:
1. Identify and discuss the key similarities between the two events.
2. Identify and discuss the key differences between the two events.
3. Explain the causes of each event and how they influenced the outcomes.
4. Discuss the effects of each event on society and their long-term impacts.

Submit your analysis as a plain text string. Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of the historical events."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should identify key similarities between the two events.",
            "The analysis should identify key differences between the two events.",
            "The analysis should explain the causes of each event and how they influenced the outcomes.",
            "The analysis should discuss the effects of each event on society and their long-term impacts.",
            "The response should be well-structured, coherent, and demonstrate a deep understanding of the historical events."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
