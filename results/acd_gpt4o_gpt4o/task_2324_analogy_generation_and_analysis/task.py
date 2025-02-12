class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept_pairs": "sun:planet, teacher:student"
            },
            "2": {
                "analogy": "Just as a sword is the weapon of a warrior, a pen is the weapon of a writer."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'concept_pairs' in t:
            concept_pairs = t['concept_pairs']
            instructions = f"""Your task is to generate analogies based on the provided pairs of concepts.

Concept Pairs: {concept_pairs}

For each pair of concepts, create an analogy that clearly conveys the relationship between them. Ensure that your analogies are logically sound and effectively illustrate the relationships.

Provide your analogies in plain text format, each in a separate line.

Response Format:
Analogy 1: [Your analogy for the first pair]
Analogy 2: [Your analogy for the second pair]"""
        elif 'analogy' in t:
            analogy = t['analogy']
            instructions = f"""Your task is to analyze the provided analogy and explain the relationships it conveys.

Analogy: {analogy}

Explain the relationship between the two pairs of concepts in the analogy. Ensure that your explanation is clear, detailed, and accurately describes the relationships.

Provide your response in plain text format.

Response Format:
Analysis: [Your detailed explanation of the relationships]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'concept_pairs' in t:
            criteria = [
                "The analogies should be logically sound.",
                "The analogies should effectively illustrate the relationships between the concepts.",
                "Each analogy should be presented in a separate line.",
                "The analogies should be creative and meaningful."
            ]
        elif 'analogy' in t:
            criteria = [
                "The explanation should be clear and detailed.",
                "The explanation should accurately describe the relationships between the concepts.",
                "The explanation should demonstrate a deep understanding of the analogy."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
