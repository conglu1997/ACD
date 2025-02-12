class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "events": [
                    "The signing of the Declaration of Independence (1776)",
                    "The start of the American Civil War (1861)",
                    "The end of World War II (1945)",
                    "The Moon landing (1969)"
                ]
            },
            "2": {
                "events": [
                    "The fall of the Roman Empire (476)",
                    "The beginning of the Renaissance (14th century)",
                    "The Industrial Revolution (18th-19th century)",
                    "The invention of the internet (20th century)"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following historical events and arrange them in chronological order. Then, provide a brief explanation of the significance of each event in history. Ensure your explanations are clear and concise, covering the key points of each event. Do not include the years in your final submission.

Events: {', '.join(t['events'])}

Submit your response as a plain text string in the following format:

1. [First event]: [Explanation]
2. [Second event]: [Explanation]
3. [Third event]: [Explanation]
4. [Fourth event]: [Explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The events should be arranged in correct chronological order.",
            "Each explanation should clearly state the significance of the event."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
