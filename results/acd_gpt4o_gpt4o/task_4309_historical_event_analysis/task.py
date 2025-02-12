class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event1": "The fall of the Berlin Wall in 1989",
                "event2": "The signing of the Declaration of Independence in 1776"
            },
            "2": {
                "event1": "The moon landing in 1969",
                "event2": "The invention of the printing press in the 15th century"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze and compare the following two historical events. Interpret their significance and impact on society.

Event 1: {t['event1']}
Event 2: {t['event2']}

Your response should include:
1. A detailed analysis of each event's significance.
2. A comparison of the two events, highlighting similarities and differences in their impact.
3. An explanation of which event you believe had a greater impact on society and why.

Provide your response in plain text format, structured in paragraphs as follows:

Analysis of Event 1: [Your analysis]
Analysis of Event 2: [Your analysis]
Comparison: [Your comparison]
Greater Impact: [Your explanation]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be detailed and cover the significance of each event.",
            "The comparison should highlight similarities and differences between the events.",
            "The explanation should state which event had a greater impact and provide reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
