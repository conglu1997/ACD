class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a timeline based on the following historical events and describe each event in one sentence.",
                "events": [
                    "The fall of the Berlin Wall",
                    "The moon landing",
                    "The signing of the Declaration of Independence",
                    "The start of World War II"
                ],
                "format": "Event: Description"
            },
            "2": {
                "description": "Analyze the following timeline for accuracy and coherence. Correct any errors and provide a brief explanation for each correction.",
                "timeline": [
                    "1969: The fall of the Berlin Wall",
                    "1945: The start of World War II",
                    "1776: The signing of the Declaration of Independence",
                    "1961: The moon landing"
                ],
                "corrected_timeline": [
                    "1776: The signing of the Declaration of Independence",
                    "1939: The start of World War II",
                    "1969: The moon landing",
                    "1989: The fall of the Berlin Wall"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "events" in t:
            return f"""Generate a timeline based on the following historical events. For each event, provide a one-sentence description.

Events: {', '.join(t['events'])}

Ensure your timeline is in chronological order and each event is accurately described. Submit your response as a plain text string in the following format:

Event: Description
..."""
        elif "timeline" in t:
            return f"""Analyze the following timeline for accuracy and coherence. Correct any errors and provide a brief explanation for each correction.

Timeline:
{chr(10).join(t['timeline'])}

Submit your corrected timeline and explanations as a plain text string in the following format:

Corrected Timeline:
Event: Description
...

Corrections:
Explanation
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "corrected_timeline" in t:
            validation_criteria = [
                "The corrected timeline should be in chronological order.",
                "Each event should be accurately described.",
                "The explanations for corrections should be clear and logical."
            ]
        else:
            validation_criteria = [
                "The timeline should be in chronological order.",
                "Each event should be accurately described."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
