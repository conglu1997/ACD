class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    {"year": 1776, "description": "Declaration of Independence signed in the United States."},
                    {"year": 1789, "description": "French Revolution begins."},
                    {"year": 1804, "description": "Napoleon Bonaparte crowns himself Emperor of France."}
                ]
            },
            "2": {
                "events": [
                    {"year": 1914, "description": "World War I begins."},
                    {"year": 1917, "description": "Russian Revolution leads to the downfall of the Tsar."},
                    {"year": 1918, "description": "World War I ends with the signing of the Treaty of Versailles."}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events = t['events']
        events_str = "\n".join([f"- {event['year']}: {event['description']}" for event in events])
        return f"""Reconstruct a timeline and provide a detailed narrative for the following historical events:\n{events_str}\nYour response should include:\n1. A chronological timeline of the events.\n2. A detailed narrative explaining the significance of each event and how they are interconnected.\nEnsure that your narrative is historically accurate, coherent, and well-explained. Format your response as follows:\n\nTimeline:\n- [Year]: [Event Description]\nNarrative:\n[Detailed narrative]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The timeline should be chronological.",
            "The narrative should explain the significance of each event.",
            "The narrative should explain how the events are interconnected.",
            "The narrative should be historically accurate and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
