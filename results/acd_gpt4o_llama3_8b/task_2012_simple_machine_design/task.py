class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'problem': 'Lift a 50 kg weight to a height of 2 meters using a lever. Describe the type of lever, the placement of the fulcrum, the length of the lever arms, and the required force. Assume the lever is frictionless and the weight is lifted at a constant speed. Include appropriate units in your calculations.'
            },
            '2': {
                'problem': 'Move a 100 kg object up a 5-meter incline with an angle of 30 degrees. Describe the inclined plane, calculate the force needed to move the object assuming no friction, and calculate the work done in moving the object. Include appropriate units in your calculations.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a simple machine to solve the given problem. Provide a detailed description of the machine, including its components and how it operates. Explain the principles of physics involved and any calculations needed to justify your design.

Problem: {t['problem']}

Your response should include:
1. A detailed description of the machine and its components.
2. An explanation of how the machine operates to solve the problem.
3. Any relevant physics principles and calculations used to justify your design. Be sure to include appropriate units in your calculations.

Submit your response as a plain text string in the following format:
- Description: [Your description here]
- Operation: [Your explanation here]
- Calculations: [Your calculations here]

Ensure your response is clear, precise, and demonstrates a solid understanding of mechanical reasoning and physics principles."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            'The description should accurately describe the machine and its components.',
            'The explanation should clearly detail how the machine operates to solve the problem.',
            'The calculations should be correct, include appropriate units, and demonstrate an understanding of relevant physics principles.',
            'The overall response should be coherent and logically sound.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
