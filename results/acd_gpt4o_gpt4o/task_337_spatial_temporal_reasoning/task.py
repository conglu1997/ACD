class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event_sequence": "John placed the book on the table. Then, he moved the chair next to the table. After that, he sat on the chair and started reading the book. A few minutes later, he got up, walked to the window, and looked outside."
            },
            "2": {
                "event_sequence": "Sara parked her car in the garage. She entered the house and placed her keys on the kitchen counter. Later, she went to the living room to watch TV. After watching TV for an hour, she went upstairs to her bedroom."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to interpret the given sequence of events and identify the spatial and temporal relationships between them. "
            "Provide a clear and concise description of the spatial layout and the order of events as they occur. "
            "Ensure your response captures both the spatial arrangement and the sequence of actions. Provide your response in plain text format, structured as follows: \n\n"
            "1. Overall spatial layout \n"
            "2. Sequence of events \n"
            "3. Spatial relationships between key elements"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately describe the overall spatial layout.",
            "The sequence of events should be correctly identified and described.",
            "The spatial relationships between key elements should be clearly articulated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
