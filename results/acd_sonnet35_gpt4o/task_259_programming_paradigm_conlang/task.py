import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        paradigms = [
            "Object-Oriented",
            "Functional",
            "Logic",
            "Procedural"
        ]
        texts = [
            "The quick brown fox jumps over the lazy dog.",
            "To be or not to be, that is the question."
        ]
        tasks = {
            str(i+1): {
                "paradigm": random.choice(paradigms),
                "text": random.choice(texts)
            } for i in range(2)
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a constructed language (conlang) based on the {t['paradigm']} programming paradigm. Your task has four parts:

1. Language Design (200-250 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how these features reflect the principles of the {t['paradigm']} programming paradigm.
   c) Provide at least 5 example words or phrases in your conlang, with their meanings and explanations of how they embody the paradigm.

2. Grammar Rules (150-200 words):
   a) Outline the main grammatical rules of your conlang.
   b) Explain how these rules parallel concepts in the {t['paradigm']} paradigm.
   c) Provide an example sentence demonstrating these rules.

3. Translation (100-150 words):
   Translate the following text into your conlang:
   "{t['text']}"
   Provide a word-for-word gloss and explain any interesting features of the translation.

4. Analysis (150-200 words):
   a) Discuss the strengths and limitations of your conlang in expressing natural language concepts.
   b) Explain how this conlang might influence thinking patterns if it were someone's native language.
   c) Propose an application where this conlang might be particularly useful or insightful.

Ensure your response demonstrates a deep understanding of both linguistics and the specified programming paradigm. Be creative in your language design while maintaining logical consistency with the paradigm's principles.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang should clearly reflect principles of the {t['paradigm']} programming paradigm.",
            "The language design should be creative, coherent, and well-explained.",
            "The grammar rules should be logically consistent and parallel to the programming paradigm.",
            f"The translation of '{t['text']}' should be provided and adequately explained.",
            "The analysis should offer insightful reflections on the conlang's properties and potential applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
