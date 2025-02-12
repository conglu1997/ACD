class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The Fall of the Berlin Wall",
                "perspective": "a young East German citizen witnessing the event"
            },
            "2": {
                "historical_event": "The Moon Landing",
                "perspective": "a scientist working at NASA during the event"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical event and write a short piece (200-300 words) from the perspective of a person from that time. Ensure your piece is historically accurate and captures the emotions and thoughts of the person in that context. Maintain historical accuracy without giving away the solution.

Historical Event: {t['historical_event']}
Perspective: {t['perspective']}

Submit your response as a plain text string in the following format:

Response: [Your short piece here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The piece should be historically accurate.",
            "The piece should capture the emotions and thoughts of the person in that context.",
            "The writing should be coherent and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
