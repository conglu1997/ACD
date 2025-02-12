import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept": "prime numbers",
                "message": "The universe is expanding",
                "decode": "2 3 5 7 11 13 17 19 23 29"
            },
            {
                "concept": "geometric sequences",
                "message": "Knowledge grows exponentially",
                "decode": "2 4 8 16 32 64 128 256 512 1024"
            },
            {
                "concept": "Fibonacci sequence",
                "message": "Nature follows mathematical patterns",
                "decode": "1 1 2 3 5 8 13 21 34 55"
            },
            {
                "concept": "perfect squares",
                "message": "Symmetry is fundamental to physics",
                "decode": "1 4 9 16 25 36 49 64 81 100"
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language based on the mathematical concept of {t['concept']}. Your task is to:

1. Create a system for representing words or concepts using {t['concept']}. Explain how your system works (3-4 sentences).

2. Provide a set of basic rules for forming sentences in your language (at least 3 rules).

3. Translate the following message into your language: "{t['message']}"

4. Explain how your translation reflects the mathematical concept and the rules you've created (2-3 sentences).

5. Decode the following message in your language: {t['decode']}
   Explain your decoding process (2-3 sentences).

6. Describe how your language could be used to express a complex mathematical or scientific idea that would be difficult to convey in natural languages (3-4 sentences).

Ensure your language system is logically consistent, creative, and clearly demonstrates the use of {t['concept']} in its structure and function.

Provide your response in the following format:

1. Language System:
[Your explanation here]

2. Rules:
- Rule 1: [Description]
- Rule 2: [Description]
- Rule 3: [Description]

3. Translation:
[Your translation of the given message]

4. Translation Explanation:
[Your explanation here]

5. Decoding:
[Your decoded message]
Decoding Process: [Your explanation]

6. Complex Idea Expression:
[Your description here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language system clearly and creatively incorporates the concept of {t['concept']}",
            "At least three logically consistent and well-explained rules for forming sentences are provided",
            f"The translation of '{t['message']}' follows the given rules and reflects the mathematical concept",
            f"The decoding of '{t['decode']}' is correct and the process is well-explained",
            "The explanation of how to express complex ideas in this language is creative, plausible, and demonstrates the language's unique capabilities",
            "The overall language design is unique, logically consistent, and demonstrates a deep understanding of the mathematical concept",
            "The response follows the specified format exactly"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
