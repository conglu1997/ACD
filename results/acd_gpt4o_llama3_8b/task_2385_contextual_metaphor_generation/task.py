class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'context': 'Overcoming challenges in life'},
            '2': {'metaphor': 'A rolling stone gathers no moss.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'context' in t:
            return f"Generate a new metaphor based on the following context: {t['context']}\n\nYour response should include:\n1. The metaphor.\n2. A brief explanation of the metaphor's meaning and how it relates to the given context.\n\nSubmit your response as a plain text string in the following format:\n\nMetaphor: [Your metaphor]\nExplanation: [Your explanation]"
        elif 'metaphor' in t:
            return f"Interpret the following metaphor in detail: {t['metaphor']}\n\nYour response should include:\n1. A literal translation of the metaphor.\n2. An explanation of the metaphor's deeper meaning and significance.\n3. Examples of how this metaphor can be applied in different contexts.\n\nSubmit your response as a plain text string in the following format:\n\nLiteral Translation: [Your literal translation]\nExplanation: [Your explanation]\nExamples: [Your examples]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'context' in t:
            criteria = [
                "The metaphor should be original and creative.",
                "The explanation should clearly relate the metaphor to the given context."
            ]
        elif 'metaphor' in t:
            criteria = [
                "The literal translation should capture the essence of the metaphor.",
                "The explanation should provide a deep understanding of the metaphor's significance.",
                "The examples should demonstrate the metaphor's applicability in different contexts."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
