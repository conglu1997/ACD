import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Celestial Nomads",
                "description": "A culture of space-faring nomads who navigate by starlight and cosmic phenomena."
            },
            {
                "name": "Quantum Monks",
                "description": "A secluded society of monks who base their philosophy on quantum mechanics principles."
            },
            {
                "name": "Chrono-Agriculturists",
                "description": "A civilization of farmers who manipulate localized time fields to optimize crop growth."
            }
        ]
        return {str(i+1): culture for i, culture in enumerate(random.sample(cultures, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a unique number system for the {t['name']} culture, who are described as: {t['description']}. Then use this number system to solve a mathematical problem and analyze its cultural implications. Follow these steps:

1. Number System Design (200-250 words):
   a) Create a base number system (e.g., base-8, base-12) that reflects the culture's characteristics.
   b) Describe the symbols or representations used for digits, ensuring they are culturally relevant.
   c) Explain any special numbers or numerical concepts unique to this culture.
   d) Provide examples of how basic numbers (0-10) would be represented in this system.
   e) Explain how basic arithmetic operations work in this system.

2. Mathematical Problem (150-200 words):
   a) Present a mathematical problem relevant to the culture's lifestyle or beliefs.
   b) Solve the problem using your created number system.
   c) Explain your solution process step by step, showing all work and calculations.

3. Cultural Analysis (200-250 words):
   a) Explain how this number system reflects the values and lifestyle of the culture.
   b) Describe how this system might influence the culture's scientific or technological development.
   c) Discuss any taboos, superstitions, or sacred concepts related to numbers in this culture.
   d) Provide at least two concrete examples of how this number system would be used in daily life.

4. Comparative Reflection (150-200 words):
   a) Compare your number system to our decimal system, highlighting key differences and similarities.
   b) Discuss one advantage and one limitation of your system compared to the decimal system.
   c) Propose a real-world scenario where your number system might be more efficient or useful than the decimal system.
   d) Provide a specific example illustrating this efficiency or usefulness.

Ensure your response demonstrates a deep understanding of mathematical principles, cultural anthropology, and creative problem-solving. Be innovative in your design while maintaining internal consistency and cultural relevance.

Please structure your response using the following headers:

# 1. Number System Design

# 2. Mathematical Problem

# 3. Cultural Analysis

# 4. Comparative Reflection

Make sure to address all points under each header and adhere to the word count guidelines for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must create a unique number system for the {t['name']} culture that logically reflects the culture's characteristics",
            "The number system design must include symbols, special numbers, and examples of basic numbers and arithmetic operations",
            "The mathematical problem must be culturally relevant, solved using the created number system, with a clear step-by-step explanation",
            "The cultural analysis must demonstrate how the number system influences and is influenced by the culture, with concrete examples of its use in daily life",
            "The comparative reflection must provide insightful comparisons with the decimal system, including advantages, limitations, and a specific example of increased efficiency or usefulness",
            "The response should be well-organized using the provided headers and adhere to the word count guidelines for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
