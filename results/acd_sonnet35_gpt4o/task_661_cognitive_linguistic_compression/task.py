import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "chunking",
            "semantic networks",
            "spreading activation",
            "priming effects",
            "hierarchical processing"
        ]
        return {
            "1": {"principle": random.choice(cognitive_principles)},
            "2": {"principle": random.choice(cognitive_principles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a text compression algorithm inspired by the cognitive principle of {t['principle']}. Your task has the following parts:

1. Algorithm Design (200-250 words):
   a) Explain how the cognitive principle of {t['principle']} informs your compression algorithm.
   b) Describe the step-by-step process of your compression algorithm.
   c) Discuss how your algorithm might differ from traditional compression methods.

2. Linguistic Analysis (150-200 words):
   a) Analyze how your algorithm interacts with different linguistic features (e.g., syntax, semantics, pragmatics).
   b) Predict which types of text your algorithm might be most effective for, and why.

3. Compression Example:
   Provide a simple example of compressing a short text (50-100 words) using your algorithm. Show the steps and the compressed output.

4. Cognitive Load Analysis (100-150 words):
   Discuss how your compression algorithm might affect cognitive load during decompression and reading of the text.

5. Potential Applications (100-150 words):
   Propose two novel applications of your cognitive-linguistic compression algorithm outside of standard data compression scenarios.

Ensure your response demonstrates a deep understanding of both cognitive science and computational linguistics. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (e.g., '1. Algorithm Design', '2. Linguistic Analysis', etc.)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the given cognitive principle and its application to text compression.",
            "The proposed algorithm is innovative and differs from traditional compression methods.",
            "The linguistic analysis shows insight into how the algorithm interacts with various language features.",
            "The compression example is clear and demonstrates the algorithm's functionality.",
            "The cognitive load analysis and potential applications are thoughtful and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
