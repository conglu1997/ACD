import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        texts = [
            "The quick brown fox jumps over the lazy dog.",
            "To be or not to be, that is the question.",
            "I think, therefore I am."
        ]
        programming_concepts = [
            "object-oriented programming",
            "functional programming",
            "logic programming"
        ]
        tasks = [
            {"text": text, "concept": concept}
            for text, concept in zip(texts, programming_concepts)
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel writing system inspired by {t['concept']}. Your task is to:

1. Conceptual Design (200-250 words):
   a) Explain how your writing system incorporates key principles from {t['concept']}.
   b) Describe the basic elements of your writing system (e.g., symbols, structures, rules).
   c) Discuss how your system represents different parts of speech or grammatical functions.

2. Alphabet or Symbol Set (100-150 words):
   a) Present a basic alphabet or symbol set for your writing system.
   b) Explain the logic behind your symbols and how they relate to {t['concept']}.

3. Grammar and Syntax (150-200 words):
   a) Outline the fundamental grammar rules of your writing system.
   b) Explain how sentence structure in your system reflects principles of {t['concept']}.

4. Translation (100-150 words):
   Translate the following text into your writing system: "{t['text']}"
   Provide both a visual representation and a detailed explanation of your translation process.

5. Analysis (150-200 words):
   a) Discuss the strengths and limitations of your writing system.
   b) Explain how your system might change the way we think about or process written language.
   c) Propose a potential real-world application for your writing system.

Ensure your response is creative, logically consistent, and demonstrates a deep understanding of both linguistic principles and {t['concept']}. Use appropriate terminology from both fields in your explanation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The writing system clearly incorporates principles from {t['concept']}",
            "The alphabet or symbol set is logically designed and explained",
            "The grammar and syntax rules are well-defined and reflect the chosen programming concept",
            f"The translation of '{t['text']}' is provided and thoroughly explained",
            "The analysis demonstrates critical thinking about the system's implications and applications",
            "The response shows creativity and originality in bridging linguistics and programming concepts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
