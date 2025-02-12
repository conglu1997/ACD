class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'statement': 'Prove that the sum of the angles in a triangle is 180 degrees.', 'proof_text': 'Given a triangle ABC, draw a line parallel to the base BC through the vertex A. This creates two alternate interior angles with the angles at B and C, which sum to the angle at A. Therefore, the sum of the angles in triangle ABC is 180 degrees.'},
            '2': {'statement': 'Prove that the square root of 2 is irrational.', 'proof_text': 'Assume that √2 is rational, meaning it can be written as a fraction a/b in its simplest form. Then 2 = a^2/b^2, or a^2 = 2b^2. This implies that a^2 is even, so a must be even. Let a = 2k. Then (2k)^2 = 2b^2, or 4k^2 = 2b^2, which simplifies to b^2 = 2k^2. This implies that b^2 is even, so b must be even. But this contradicts the assumption that a/b is in its simplest form. Therefore, √2 is irrational.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: creation and analysis.

Part 1: Creation
Using the given statement, create a mathematical proof that demonstrates the truth of the statement. Ensure your proof is logically sound, clearly articulated, and follows standard mathematical conventions. Provide your proof in plain text format.

Statement: {t['statement']}

Your response format:
Proof: [Your mathematical proof]

Part 2: Analysis
Analyze the provided mathematical proof. Identify any logical steps, mathematical principles used, and the overall coherence of the proof. Provide your analysis in plain text format.

Provided Proof: {t['proof_text']}

Your response format:
Analysis: [Your analysis of the proof]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The created proof should be logically sound and clearly articulated.',
            'The proof should follow standard mathematical conventions.',
            'The analysis should correctly identify logical steps, mathematical principles used, and the coherence of the provided proof.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
