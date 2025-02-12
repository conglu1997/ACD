import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            "prime numbers",
            "Fibonacci sequence",
            "complex numbers",
            "modular arithmetic",
            "fractal geometry",
            "group theory",
            "topology",
            "linear algebra"
        ]
        linguistic_features = [
            "phonology",
            "morphology",
            "syntax",
            "semantics",
            "pragmatics",
            "orthography",
            "lexicon",
            "discourse structure"
        ]
        messages = [
            "The universe speaks in numbers",
            "Mathematics is the language of nature",
            "Patterns emerge from chaos",
            "Infinity lies within the finite"
        ]
        return {
            "1": {"math_concept": random.choice(math_concepts), "linguistic_feature": random.choice(linguistic_features), "message": random.choice(messages)},
            "2": {"math_concept": random.choice(math_concepts), "linguistic_feature": random.choice(linguistic_features), "message": random.choice(messages)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 40 minutes to complete this task. Design a constructed language (conlang) based on the mathematical concept of {t['math_concept']}, focusing primarily on the linguistic feature of {t['linguistic_feature']}. Then, use your conlang to encode a given message and analyze its properties. Your task has the following parts:

1. Conlang Design (250-300 words):
   a) Explain how you will incorporate {t['math_concept']} into the {t['linguistic_feature']} of your conlang.
   b) Describe the basic rules and structure of your conlang, providing examples.
   c) Discuss how your conlang's mathematical basis affects its expressive capabilities.

2. Vocabulary and Grammar (150-200 words):
   a) Create a mini-lexicon of at least 10 words or morphemes in your conlang.
   b) Explain how these words/morphemes reflect the mathematical properties of your language.
   c) Provide 2-3 example sentences in your conlang, with translations and explanations of their structure.

3. Message Encoding (200-250 words):
   Encode the following message in your conlang: "{t['message']}"
   a) Show the encoded message in your conlang.
   b) Explain the encoding process step-by-step.
   c) Discuss any challenges in expressing this message in your mathematically-based language.

4. Mathematical Analysis (200-250 words):
   a) Analyze the information density of your conlang compared to natural languages.
   b) Discuss any interesting mathematical properties that emerge from your language design.
   c) Propose a mathematical formula or algorithm that could generate valid sentences in your conlang.

5. Linguistic Implications (150-200 words):
   a) Discuss how your conlang might influence or constrain thought processes if it were used as a primary language.
   b) Compare your conlang to existing philosophical or logical languages (e.g., Lojban, Ithkuil).
   c) Propose an experiment to test the cognitive effects of using your conlang.

Ensure your response demonstrates a deep understanding of both linguistics and mathematics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining logical consistency and mathematical rigor.

Format your response using the following structure:

1. Conlang Design
[Your design explanation here]

2. Vocabulary and Grammar
[Your vocabulary and grammar description here]

3. Message Encoding
[Your encoded message and explanation here]

4. Mathematical Analysis
[Your analysis here]

5. Linguistic Implications
[Your discussion here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design effectively incorporates {t['math_concept']} into {t['linguistic_feature']}.",
            "The vocabulary and grammar rules are logically consistent and reflect the mathematical basis of the language.",
            "The message encoding process is clear and demonstrates the language's unique properties.",
            "The mathematical analysis provides insightful observations about the conlang's properties.",
            "The discussion of linguistic implications is thoughtful and grounded in existing language philosophy.",
            "The response demonstrates creativity, interdisciplinary knowledge, and analytical skills.",
            "The submission follows the specified format structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
