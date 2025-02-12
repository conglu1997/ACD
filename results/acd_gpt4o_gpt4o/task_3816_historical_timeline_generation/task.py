class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    {"event": "Fall of the Western Roman Empire", "year": 476},
                    {"event": "Signing of the Magna Carta", "year": 1215},
                    {"event": "Christopher Columbus reaches the Americas", "year": 1492},
                    {"event": "Start of the Protestant Reformation", "year": 1517}
                ]
            },
            "2": {
                "events": [
                    {"event": "American Declaration of Independence", "year": 1776},
                    {"event": "French Revolution begins", "year": 1789},
                    {"event": "Start of the Industrial Revolution", "year": 1760},
                    {"event": "End of World War I", "year": 1918}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events_list = ', '.join([f"{{event['event']}} ({{event['year']}})" for event in t['events']])
        return f"""Your task is to generate a coherent and accurate timeline based on the following set of historical events:

Events: {events_list}

The timeline should include the following sections:
1. Ordered List of Events: List all the events in chronological order.
2. Detailed Descriptions: Provide a brief description of each event, including its significance and any relevant contextual information.

Ensure that the timeline is clear, logically ordered, and historically accurate.

Format your response as follows:
Ordered List of Events: <your ordered list>
Detailed Descriptions: <your detailed descriptions>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The events should be listed in chronological order.",
            "Each event should have a brief description including its significance.",
            "The timeline should be clear and logically ordered.",
            "The historical information should be accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
