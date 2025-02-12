class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"question": "Explain the concept of a major scale and list the notes in a C major scale."},
            "2": {"question": "Describe the difference between a major chord and a minor chord, and provide examples of each in the key of G."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze and explain the following music theory concept. Ensure your explanation is clear, accurate, and comprehensive.

Question: {t['question']}

Instructions:
1. Understand the music theory concept presented in the question.
2. Provide a detailed explanation of the concept, covering all relevant aspects.
3. Include examples to illustrate your explanation. For scales, list all the notes; for chords, provide the notes that make up the chords.
4. Ensure your response is structured and in plain text format.

Your response should be in the following format:

Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and accurate.",
            "The response should include relevant examples.",
            "The response should cover all aspects of the question in detail.",
            "The response should be well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
