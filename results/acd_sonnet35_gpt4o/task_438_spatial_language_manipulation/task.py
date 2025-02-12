import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "objects": ["cube", "sphere", "pyramid"],
                "initial_state": "The cube is on top of the sphere. The pyramid is to the right of the sphere.",
                "operations": [
                    "Move the cube to the left of the sphere.",
                    "Place the pyramid on top of the cube."
                ]
            },
            {
                "objects": ["book", "lamp", "vase"],
                "initial_state": "The book is under the lamp. The vase is in front of the lamp.",
                "operations": [
                    "Move the vase behind the lamp.",
                    "Place the book on top of the vase."
                ]
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret and manipulate the spatial relationships described in the following scenario:

Initial state: {t['initial_state']}

Perform the following operations in order:
1. {t['operations'][0]}
2. {t['operations'][1]}

Your task:
1. Describe the final arrangement of the objects after performing these operations. Be precise and use clear spatial language.
2. Create a simple ASCII art representation of the final arrangement.
3. List any ambiguities or assumptions you had to make in interpreting the spatial relationships or operations.

Format your response as follows:
Final Arrangement: [Your description]

ASCII Representation:
[Your ASCII art]

Ambiguities/Assumptions: [Your list]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The final arrangement description accurately reflects the initial state and operations performed.",
            "The ASCII art representation is clear and consistent with the described final arrangement.",
            "Any relevant ambiguities or assumptions are identified and explained.",
            "The response demonstrates a strong understanding of spatial relationships and their linguistic descriptions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
