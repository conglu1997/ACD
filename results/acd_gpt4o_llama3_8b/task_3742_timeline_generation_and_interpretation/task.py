class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "timeline": [
                    "1776: Declaration of Independence",
                    "1783: End of the American Revolutionary War",
                    "1787: Drafting of the U.S. Constitution",
                    "1789: George Washington becomes the first President of the United States"
                ],
                "instruction": "Interpret the given historical timeline and describe the sequence of events in plain text. The description should include the year and a brief explanation of each event. Format your response as follows: 'In [year], [event].'"
            },
            "2": {
                "events": [
                    "Fall of the Berlin Wall",
                    "Moon landing",
                    "Invention of the World Wide Web",
                    "First manned spaceflight",
                    "End of World War II"
                ],
                "instruction": "Generate a timeline for the given events. Ensure the events are placed in the correct chronological order and provide the year when each event occurred. Format your response as follows: '[year]: [event], [year]: [event], ...'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "timeline" in t:
            return f"Interpret the following historical timeline and describe the sequence of events in plain text. The description should include the year and a brief explanation of each event. Format your response as follows: 'In [year], [event].'\n\nTimeline: {', '.join(t['timeline'])}"
        else:
            return f"Generate a timeline for the given events. Ensure the events are placed in the correct chronological order and provide the year when each event occurred. Format your response as follows: '[year]: [event], [year]: [event], ...'\n\nEvents: {', '.join(t['events'])}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "timeline" in t:
            criteria = [
                "The description should accurately reflect the sequence of events and their respective years.",
                "The response should provide a brief explanation of each event."
            ]
        else:
            criteria = [
                "The generated timeline should place events in the correct chronological order.",
                "The response should include the accurate year for each event."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
