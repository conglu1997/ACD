import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        number_properties = [
            {"property": "prime", "range": (2, 100), "definition": "a number greater than 1 that has no positive divisors other than 1 and itself"},
            {"property": "perfect", "range": (1, 10000), "definition": "a positive integer that is equal to the sum of its proper positive divisors"},
            {"property": "fibonacci", "range": (1, 100), "definition": "a number in the sequence where each number is the sum of the two preceding ones"},
            {"property": "triangular", "range": (1, 100), "definition": "a number that can be represented as a triangular array of points"}
        ]
        return {
            "1": random.choice(number_properties),
            "2": random.choice(number_properties)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) for expressing mathematical concepts, with a focus on creating a numeral system that encodes the property of {t['property']} numbers. For reference, a {t['property']} number is defined as {t['definition']}.

Your task has the following components:

1. Numeral System Design (250-300 words):
   a) Create a unique numeral system that visually or structurally encodes whether a number is {t['property']} or not.
   b) Explain the rules and structure of your numeral system.
   c) Provide examples of how your system represents at least five numbers (including both {t['property']} and non-{t['property']} numbers) within the range {t['range']}.
   d) Explain how your system makes it easy to identify {t['property']} numbers.

2. Mathematical Vocabulary (200-250 words):
   a) Create 5-7 mathematical terms in your conlang related to the concept of {t['property']} numbers.
   b) Provide their English translations and explain the logic behind your word construction.
   c) Demonstrate how these terms can be used in a mathematical statement or theorem.

3. Syntax and Grammar (150-200 words):
   a) Describe the basic syntax and grammar rules of your conlang for expressing mathematical operations and relationships.
   b) Explain how your language handles mathematical proofs or logical arguments.
   c) Provide an example sentence or expression in your conlang with an English translation.

4. Problem Solving (200-250 words):
   a) Present a mathematical problem or theorem related to {t['property']} numbers in your conlang.
   b) Provide step-by-step solution or proof in your conlang.
   c) Explain how your conlang facilitates the problem-solving process for this type of mathematical concept.

5. Comparative Analysis (100-150 words):
   Compare your mathematical conlang to existing mathematical notation systems, highlighting its unique features and potential advantages for working with {t['property']} numbers.

Ensure your response demonstrates a deep understanding of both linguistic structures and mathematical concepts. Be creative in your language design while maintaining mathematical rigor and clarity. Use appropriate terminology from both linguistics and mathematics, providing clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 900-1150 words. Please adhere to this word count range in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed numeral system that clearly encodes the property of {t['property']} numbers.",
            "The mathematical vocabulary is creative, logical, and relevant to the given number property.",
            "The conlang's syntax and grammar rules are clearly explained and suitable for mathematical expressions.",
            f"A mathematical problem related to {t['property']} numbers is presented and solved using the conlang.",
            "The comparative analysis highlights unique features of the conlang for mathematical concepts.",
            "The overall design demonstrates a deep understanding of both linguistics and mathematics.",
            "The response adheres to the specified word count range of 900-1150 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
