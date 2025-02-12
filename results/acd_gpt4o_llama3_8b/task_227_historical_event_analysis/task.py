class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event_1": "The fall of the Roman Empire",
                "event_2": "The fall of Constantinople"
            },
            "2": {
                "event_1": "The American Revolution",
                "event_2": "The French Revolution"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical events and provide a comparative analysis. Discuss the causes, key figures, significant outcomes, and long-term impacts of each event. Highlight similarities and differences between the two events. Provide specific examples or evidence to support your analysis.\n\nEvent 1: {t['event_1']}\nEvent 2: {t['event_2']}\n\nFormat your response as follows:\n1. Introduction\n2. Analysis of Event 1\n3. Analysis of Event 2\n4. Comparative Analysis\n5. Conclusion\nYour response should be detailed and well-structured, drawing on historical knowledge and analytical skills. Ensure clarity and coherence in your writing. Each section should provide in-depth insights and use specific historical evidence to support your points."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an introduction, analysis of both events, comparative analysis, and conclusion.",
            "The analysis should discuss causes, key figures, significant outcomes, and long-term impacts of each event.",
            "The comparative analysis should highlight similarities and differences between the two events.",
            "The response should provide specific examples or evidence to support the analysis.",
            "The response should be detailed, well-structured, and coherent.",
            "Each section should provide in-depth insights and use specific historical evidence to support points."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
