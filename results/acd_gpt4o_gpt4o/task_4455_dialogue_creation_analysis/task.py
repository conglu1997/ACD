class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Two friends discussing their plans for a weekend trip to the mountains. One friend is enthusiastic, while the other is hesitant due to a fear of heights."},
            "2": {"scenario": "A detective interrogating a suspect in a robbery case. The suspect is nervous and evasive, while the detective is calm and methodical."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a fictional dialogue based on the following scenario:

{t['scenario']}

Ensure that the dialogue is coherent, contextually appropriate, and engaging. Each character's lines should reflect their personality and the given scenario. Provide your response in plain text format.

Response Format:
Character 1: [Dialogue line]
Character 2: [Dialogue line]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The dialogue should be coherent and contextually appropriate.",
            "Each character's lines should reflect their personality and the given scenario.",
            "The dialogue should be engaging and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
