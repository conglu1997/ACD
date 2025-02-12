class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dilemma": "You are a doctor in a small village with limited medical supplies. A deadly outbreak has occurred, and you have only enough medicine to save one person. There are two patients: one is a young child with their whole life ahead of them, and the other is a renowned scientist working on a cure for the outbreak. Both are in critical condition and need immediate treatment. Who do you save and why?"
            },
            "2": {
                "dilemma": "You are the captain of a spaceship on a deep-space mission. The ship's life support system is failing, and there is only enough oxygen left to sustain one person until rescue arrives. You must choose between saving yourself or a crew member who is a parent to young children back on Earth. The crew member is also the ship's chief engineer and might be able to help with repairs. Who do you save and why?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Simulate and resolve the following ethical dilemma in a narrative format.

Dilemma: {t['dilemma']}

Your response should include:
1. A detailed narrative explaining the situation.
2. The decision you make and the reasoning behind it.
3. An exploration of the potential consequences of your decision.
4. Ensure your narrative is clear, empathetic, and logically consistent.

Submit your response as a plain text string in the following format:
- Narrative: [Your narrative here]
- Decision: [Your decision here]
- Reasoning: [Your reasoning here]
- Consequences: [Your exploration of consequences here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The narrative should clearly describe the ethical dilemma and the context.",
            "The decision should be logically explained and empathetic.",
            "The reasoning should demonstrate an understanding of moral complexities.",
            "The exploration of consequences should be thorough and well-reasoned.",
            "The response should follow the specified format precisely."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
