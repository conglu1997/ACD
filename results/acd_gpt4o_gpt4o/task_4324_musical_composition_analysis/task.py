class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"composition": "Fur Elise by Ludwig van Beethoven"},
            "2": {"composition": "Canon in D by Johann Pachelbel"}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given musical composition, identifying key musical elements and providing a critical evaluation:

Composition: {t['composition']}

1. Identify the key musical elements of the composition, including the key signature, time signature, main motifs, and any notable use of harmony or rhythm.
2. Provide a critical evaluation of the piece, discussing its historical context, emotional impact, and any unique or innovative aspects. Ensure your evaluation is well-structured, detailed, and demonstrates a deep understanding of music theory.

Provide your response in the following format:

Musical Elements: [Your identification of key elements]
Critical Evaluation: [Your critical evaluation]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include identification of key musical elements such as key signature, time signature, main motifs, and notable use of harmony or rhythm.",
            "The critical evaluation should discuss the historical context, emotional impact, and unique or innovative aspects of the piece."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
