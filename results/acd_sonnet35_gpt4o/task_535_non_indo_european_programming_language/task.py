import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "language_family": "Bantu languages",
                "key_feature": "noun class system"
            },
            "2": {
                "language_family": "Austronesian languages",
                "key_feature": "verb-initial word order"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical programming language based on the grammatical structures of the {t['language_family']}, focusing on their {t['key_feature']}. Your task is to:

1. Briefly explain the key grammatical features of the {t['language_family']}, with a focus on the {t['key_feature']} (2-3 sentences).

2. Design the basic syntax of your programming language, incorporating the {t['key_feature']} in a meaningful way. Provide examples of how basic programming constructs (e.g., variable declaration, function definition, conditional statements) would be expressed in your language (5-6 sentences with code examples).

3. Explain how your language's syntax reflects the grammatical structures of the {t['language_family']}, and how it differs from traditional programming languages (3-4 sentences).

4. Describe a unique feature or capability of your programming language that arises from its basis in the {t['language_family']} (2-3 sentences).

5. Discuss potential advantages and challenges of using your language for programming, compared to traditional programming languages (3-4 sentences).

6. Provide a short example program in your language that demonstrates its unique features (5-10 lines of code with explanation).

7. Speculate on how programming in this language might influence a programmer's problem-solving approach or cognitive patterns (2-3 sentences).

Ensure your response is well-reasoned, creative, and grounded in both linguistic and computer science principles. Organize your answer using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response explains key grammatical features of {t['language_family']}, focusing on the {t['key_feature']}",
            "The basic syntax of the programming language is designed and explained with examples",
            f"The language's syntax reflects the grammatical structures of {t['language_family']} and differs from traditional programming languages",
            "A unique feature or capability of the language is described",
            "Potential advantages and challenges of using the language are discussed",
            "A short example program demonstrating unique features is provided",
            "The response speculates on how programming in this language might influence problem-solving or cognitive patterns",
            "The answer demonstrates understanding of linguistics and computer science concepts",
            "The response is well-organized with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
