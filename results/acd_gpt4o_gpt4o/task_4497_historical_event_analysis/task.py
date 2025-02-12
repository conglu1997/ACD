class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "Fall of the Roman Empire",
                "related_event": "Collapse of the Soviet Union",
                "event_description": "The Fall of the Roman Empire in 476 AD marked the end of ancient Rome and the beginning of the Middle Ages in Europe.",
                "related_event_description": "The Collapse of the Soviet Union in 1991 ended the Cold War and led to the independence of 15 former Soviet republics."
            },
            "2": {
                "event": "American Revolution",
                "related_event": "French Revolution",
                "event_description": "The American Revolution (1775-1783) led to the independence of the Thirteen Colonies from British rule.",
                "related_event_description": "The French Revolution (1789-1799) was a period of radical social and political upheaval in France that ended the monarchy and led to the rise of Napoleon Bonaparte."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        event = t["event"]
        related_event = t["related_event"]
        event_description = t["event_description"]
        related_event_description = t["related_event_description"]
        instructions = f"""Your task is to analyze the following historical event and its related event. Provide a comprehensive analysis that includes:
1. The main causes of the {event}.
2. The immediate and long-term consequences of the {event}.
3. A comparison between the {event} and the {related_event}, highlighting similarities and differences in their causes and outcomes.

Event: {event}
Description: {event_description}

Related Event: {related_event}
Description: {related_event_description}

Provide your response in plain text format, ensuring that it is detailed and insightful. Your response should include:
1. Analysis of the causes of the event.
2. Analysis of the consequences of the event.
3. Comparison between the event and the related event.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a detailed analysis of the main causes of the event.",
            "The response should describe both the immediate and long-term consequences of the event.",
            "The response should include a well-reasoned comparison between the event and the related event, highlighting similarities and differences.",
            "The response should be comprehensive and insightful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
