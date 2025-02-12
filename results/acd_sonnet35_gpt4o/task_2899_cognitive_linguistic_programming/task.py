import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_principle": "conceptual metaphor",
                "programming_paradigm": "object-oriented",
                "language_family": "Indo-European"
            },
            {
                "cognitive_principle": "mental spaces",
                "programming_paradigm": "functional",
                "language_family": "Sino-Tibetan"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on cognitive linguistics principles that can generate and interpret natural language. Your language should incorporate the cognitive principle of {t['cognitive_principle']}, use a {t['programming_paradigm']} programming paradigm, and be optimized for the {t['language_family']} language family. Your response should include:

1. Language Design (300-350 words):
   a) Describe the key features of your programming language.
   b) Explain how it incorporates the specified cognitive principle.
   c) Detail how the language implements the given programming paradigm.
   d) Discuss how the language is optimized for the specified language family.

2. Syntax and Semantics (250-300 words):
   a) Provide an overview of the language's syntax, with at least three code examples.
   b) Explain the semantic structure of the language.
   c) Describe how the language handles ambiguity in natural language.

3. Natural Language Processing Capabilities (200-250 words):
   a) Explain how the language processes and generates natural language.
   b) Provide an example of how it would interpret a complex sentence.
   c) Describe a scenario where it generates natural language output.

4. Cognitive Model Integration (200-250 words):
   a) Discuss how your language models cognitive processes in language understanding.
   b) Explain how it could be used to test hypotheses in cognitive linguistics.
   c) Describe any novel insights your language might provide about language cognition.

5. Practical Applications (150-200 words):
   a) Propose three potential applications for your language in research or industry.
   b) Explain how these applications leverage the unique features of your language.

6. Limitations and Future Work (150-200 words):
   a) Discuss any limitations of your language design.
   b) Propose future enhancements or research directions.

Ensure your response demonstrates a deep understanding of cognitive linguistics, programming language design, and natural language processing. Be creative in your approach while maintaining scientific and technical plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design must clearly incorporate the cognitive principle of {t['cognitive_principle']} and use a {t['programming_paradigm']} programming paradigm.",
            f"The language should be demonstrably optimized for the {t['language_family']} language family.",
            "The syntax and semantics section must include at least three code examples and explain how ambiguity is handled.",
            "The response must demonstrate how the language processes and generates natural language, with specific examples.",
            "The cognitive model integration section should explain how the language models cognitive processes and could be used in cognitive linguistics research.",
            "The response should propose three practical applications that leverage the unique features of the language.",
            "The limitations and future work section must critically analyze the language design and propose plausible enhancements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
