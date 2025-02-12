class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "time",
                "example_metaphor": "Time is a river that flows endlessly forward."
            },
            "2": {
                "concept": "love",
                "example_metaphor": "Love is a journey with unpredictable paths."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate a metaphor for the following concept and explain its meaning and relevance:\n\nConcept: {t['concept']}\n\nYour metaphor should adhere to the following guidelines:\n1. Be creative and original.\n2. Clearly relate to the given concept.\n3. Include a detailed explanation of the metaphor's meaning and relevance.\n\nProvide your response in the following format:\nMetaphor: [Your metaphor]\nExplanation: [Your explanation]\n\nExample Response:\nConcept: Time\nMetaphor: 'Time is a river that flows endlessly forward.'\nExplanation: This metaphor suggests that time moves continuously in one direction, much like a river. It emphasizes the unstoppable and constant nature of time.\n\nConcept: Love\nMetaphor: 'Love is a journey with unpredictable paths.'\nExplanation: This metaphor likens love to a journey, highlighting its unpredictable and evolving nature. It suggests that love can take many forms and directions, much like a journey."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The metaphor is creative and original.",
            "The metaphor clearly relates to the given concept.",
            "The explanation is detailed and clearly explains the metaphor's meaning and relevance."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
