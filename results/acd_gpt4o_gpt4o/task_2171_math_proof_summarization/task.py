class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"proof": "Consider the following proof of the Pythagorean theorem using algebra:\n\n1. Consider a right-angled triangle with legs 'a' and 'b', and hypotenuse 'c'.\n2. Construct a square with side length 'a+b'.\n3. Inside this square, place four copies of the right-angled triangle.\n4. The area of the large square is (a+b)^2.\n5. The area of the four triangles is 4*(1/2)*a*b = 2ab.\n6. The remaining area inside the square, which forms a smaller square, is c^2.\n7. Therefore, (a+b)^2 = c^2 + 2ab.\n8. Expanding (a+b)^2 gives a^2 + 2ab + b^2.\n9. Equating the two expressions, we get a^2 + 2ab + b^2 = c^2 + 2ab.\n10. Subtracting 2ab from both sides, we get a^2 + b^2 = c^2.\n\nSummarize this proof in 3-4 sentences."},
            "2": {"proof": "Consider the following proof of the irrationality of the square root of 2:\n\n1. Assume the contrary, that sqrt(2) is rational.\n2. Then it can be expressed as a fraction a/b in lowest terms, where a and b are coprime integers.\n3. Therefore, sqrt(2) = a/b implies 2 = a^2 / b^2, or a^2 = 2b^2.\n4. Thus, a^2 is even, which implies a is even (since the square of an odd number is odd).\n5. Let a = 2k for some integer k. Then a^2 = 4k^2, and we have 4k^2 = 2b^2, or 2k^2 = b^2.\n6. Thus, b^2 is even, which implies b is even.\n7. But if both a and b are even, then a/b is not in lowest terms, contradicting our initial assumption.\n8. Therefore, sqrt(2) is irrational.\n\nSummarize this proof in 3-4 sentences."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Summarize the following mathematical proof while maintaining the core logic and reasoning. Your summary should be concise, retaining the essential steps and conclusions of the proof.

Proof: {t['proof']}

Provide your summary in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The summary should be concise and accurate.", "The summary should retain the core logic and reasoning of the proof.", "The summary should be in plain text and 3-4 sentences long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
