import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "problem": "Describe a sustainable energy system",
                "constraint": "The language must use a base-6 number system and have no words longer than 4 syllables"
            },
            {
                "problem": "Explain the concept of democracy",
                "constraint": "The language must be tonal and have no distinction between nouns and verbs"
            }
        ]
        return {
            "1": problems[0],
            "2": problems[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) and use it to solve a problem. Your task has the following components:

1. Language Design (300-350 words):
   a) Create a constructed language that adheres to the following constraint: {t['constraint']}
   b) Describe the phonology (sound system) of your language, including consonants, vowels, and syllable structure.
   c) Explain the morphology (word formation) and syntax (sentence structure) of your language.
   d) Provide at least 5 example words or phrases in your language, with translations.
   e) Explain how your language satisfies the given constraint.

2. Language Analysis (200-250 words):
   a) Discuss how your language differs from natural languages.
   b) Analyze potential advantages or challenges of using your language for communication.
   c) Explain how the constraint influenced your design choices.

3. Problem Solution (300-350 words):
   Using your constructed language, provide a solution to the following problem: {t['problem']}
   a) Write out your solution in your constructed language (100-150 words).
   b) Provide an English translation of your solution.
   c) Explain how features of your language were particularly useful (or challenging) in addressing this problem.

4. Linguistic Reflection (200-250 words):
   a) Discuss how designing and using this language might influence thought patterns or problem-solving approaches.
   b) Compare your experience using the constructed language to solve the problem versus using a natural language.
   c) Propose a potential real-world application for your constructed language.

Ensure your response demonstrates a deep understanding of linguistic principles and creative problem-solving. Use clear headings for each section of your response.

Your total response should be between 1000-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The constructed language adheres to the constraint: {t['constraint']}",
            "The language design is comprehensive, covering phonology, morphology, and syntax",
            "The language analysis demonstrates understanding of linguistic principles",
            f"The problem solution addresses the given problem: {t['problem']}",
            "The solution is presented in both the constructed language and English",
            "The linguistic reflection shows insight into the relationship between language and thought",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
