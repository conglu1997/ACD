class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The fall of the Berlin Wall in 1989",
                "task": "Analyze the causes and consequences of this event."
            },
            "2": {
                "events": [
                    "The American Revolution (1775-1783)",
                    "The French Revolution (1789-1799)"
                ],
                "task": "Compare and contrast these two revolutions, highlighting their similarities and differences in causes, events, and outcomes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "events" in t:
            return f"""Compare and contrast the following historical events:

Events: {', '.join(t['events'])}

Task: {t['task']}

Your response should include an analysis of the causes, key events, and outcomes of each event, as well as a comparison of their similarities and differences. Submit your response as a plain text string in the following format:

Comparison: [Your detailed comparison]"""
        else:
            return f"""Analyze the following historical event:

Event: {t['event']}

Task: {t['task']}

Your analysis should include a discussion of the causes and consequences of the event. Submit your response as a plain text string in the following format:

Analysis: [Your detailed analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = None
        if "events" in t:
            criteria = [
                "The response should include an analysis of the causes, key events, and outcomes of each event.",
                "The comparison should highlight similarities and differences.",
                "The response should be coherent and well-structured."
            ]
        else:
            criteria = [
                "The analysis should include a discussion of the causes and consequences of the event.",
                "The response should be coherent and well-structured."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
