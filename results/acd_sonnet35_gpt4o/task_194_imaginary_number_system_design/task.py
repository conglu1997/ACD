import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "base_property": "Numbers that rotate in 3D space when multiplied",
                "additional_rule": "Addition causes dimensional shifts"
            },
            {
                "base_property": "Numbers with fractal properties that change based on their magnitude",
                "additional_rule": "Division results in color properties"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel imaginary number system with the following properties:

Base Property: {t['base_property']}
Additional Rule: {t['additional_rule']}

Your task is to:

1. System Definition (150-200 words):
   - Define the fundamental units and operations of your number system.
   - Explain how the base property and additional rule are incorporated.
   - Provide at least one example of how basic arithmetic works in this system.

2. Visualization (100-150 words):
   - Describe how numbers in this system could be visually represented.
   - Explain how this visualization changes under different operations.

3. Problem Solving (100-150 words):
   - Create and solve a mathematical problem using your number system.
   - Show your work and explain each step.

4. Real-world Application (100-150 words):
   - Propose a theoretical real-world application for your number system.
   - Explain how its unique properties could be beneficial in this context.

5. Limitations and Paradoxes (100-150 words):
   - Discuss at least one limitation or paradox that arises in your number system.
   - Explain why this occurs and its implications.

Ensure your response is creative yet logically consistent. Demonstrate clear reasoning and mathematical insight throughout your answers."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The imaginary number system incorporates the base property: {t['base_property']}.",
            f"The additional rule: {t['additional_rule']} is effectively integrated into the system.",
            "The system definition is clear, logically consistent, and demonstrates mathematical creativity.",
            "The visualization description is coherent and aligns with the system's properties.",
            "The problem-solving section demonstrates correct application of the defined system.",
            "The proposed real-world application is innovative and logically connected to the system's properties.",
            "The discussion of limitations or paradoxes shows deep understanding of the implications of the system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
