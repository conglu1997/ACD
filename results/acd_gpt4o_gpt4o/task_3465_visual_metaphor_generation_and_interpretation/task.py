class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'concept': 'freedom',
                'provided_metaphor': 'A bird flying out of an open cage.'
            },
            '2': {
                'concept': 'knowledge',
                'provided_metaphor': 'A tree with deep roots and wide branches.'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task involves two parts:\n\n1. Generate a visual metaphor for the following abstract concept: {t['concept']}. Provide a detailed explanation of how the metaphor represents the concept.\n\n2. Interpret the provided visual metaphor: {t['provided_metaphor']}. Discuss its accuracy and appropriateness, and suggest any improvements if necessary.\n\nFormat your response as follows:\n\nGenerated Metaphor: [Your metaphor]\nExplanation: [Your explanation]\nInterpretation: [Your interpretation]\nSuggestions: [Your suggestions, if any]\n\nEnsure that your explanations and interpretations are detailed, insightful, and logically sound."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The generated metaphor should be creative and accurately represent the abstract concept.',
            'The explanation should clearly link the metaphor to the concept.',
            'The interpretation of the provided metaphor should be accurate and insightful.',
            'Any suggestions for improvement should be logical and enhance the metaphor.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
