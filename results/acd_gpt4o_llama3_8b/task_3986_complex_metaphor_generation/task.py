class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept1": "Time",
                "concept2": "River"
            },
            "2": {
                "concept1": "Knowledge",
                "concept2": "Tree"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a complex metaphor that connects the following two abstract concepts:

Concept 1: {t['concept1']}
Concept 2: {t['concept2']}

Provide a detailed explanation of the metaphor, illustrating the deep connection between the two concepts. Ensure your metaphor is creative, coherent, and well-articulated. Here are some guidelines to help you:

1. Originality: The metaphor should present a fresh and unique perspective, avoiding clichés.
2. Depth: The connection between the concepts should be profound, offering new insights or perspectives.
3. Clarity: The explanation should be clear, thorough, and logically coherent.
4. Relevance: Ensure the metaphor and explanation are directly related to the given concepts.

Submit your response as a plain text string in the following format:

Metaphor: [Your metaphor]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The metaphor should be creative and original.",
            "The metaphor should illustrate a deep connection between the two concepts.",
            "The explanation should be detailed and coherent.",
            "The response should be in the specified format (Metaphor: [Your metaphor] Explanation: [Your explanation]).",
            "The metaphor and explanation should be directly related to the given concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
