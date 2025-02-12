import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        logical_structures = [
            {
                "name": "Modus Ponens",
                "structure": "If P, then Q. P. Therefore, Q."
            },
            {
                "name": "Modus Tollens",
                "structure": "If P, then Q. Not Q. Therefore, not P."
            },
            {
                "name": "Hypothetical Syllogism",
                "structure": "If P, then Q. If Q, then R. Therefore, if P, then R."
            },
            {
                "name": "Disjunctive Syllogism",
                "structure": "P or Q. Not P. Therefore, Q."
            }
        ]
        return {str(i+1): structure for i, structure in enumerate(random.sample(logical_structures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Construct a short narrative that follows the logical structure of {t['name']}. The structure is as follows:

{t['structure']}

Your task is to:

1. Create a short story (3-5 sentences) that embodies this logical structure. The story should be coherent, engaging, and logically consistent.

2. Clearly identify how each part of your story corresponds to the components of the logical structure (P, Q, R, etc.).

3. Translate each logical statement in the structure into a natural language sentence that fits your story.

Provide your response in the following format:

Story:
[Your short story here]

Logical Structure Mapping:
[Explain how each part of your story maps to the logical structure]

Natural Language Translation:
[Translate each logical statement into a natural language sentence from your story]

Ensure that your story accurately reflects the given logical structure while also being creative and engaging. Pay special attention to maintaining logical consistency throughout your narrative."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent short story that follows the {t['name']} logical structure",
            "The response clearly identifies how each part of the story corresponds to the components of the logical structure",
            "The response accurately translates each logical statement into natural language sentences from the story",
            "The story is creative and engaging while accurately reflecting the given logical structure",
            "The narrative maintains logical consistency throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
