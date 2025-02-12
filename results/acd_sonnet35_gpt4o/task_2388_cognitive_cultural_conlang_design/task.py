import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_frameworks = [
            "Non-linear time perception",
            "Collective consciousness",
            "Quantum superposition thinking",
            "Synesthetic perception",
            "Fractal-based reasoning"
        ]
        cultural_aspects = [
            "Nomadic space-faring society",
            "Symbiotic ecosystem-integrated civilization",
            "Virtual reality-based social structure",
            "Hive-mind collectivist culture",
            "Multidimensional beings' society"
        ]
        return {
            "1": {"cognitive_framework": random.choice(cognitive_frameworks), "cultural_aspect": random.choice(cultural_aspects)},
            "2": {"cognitive_framework": random.choice(cognitive_frameworks), "cultural_aspect": random.choice(cultural_aspects)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) that reflects the cognitive framework of {t['cognitive_framework']} and the cultural worldview of a {t['cultural_aspect']}. Your response should include:

1. Language Overview (200-250 words):
   a) Provide a brief description of the language's key features and how they relate to the given cognitive framework and cultural aspect.
   b) Explain the language's unique approach to expressing time, space, identity, or other fundamental concepts.
   c) Describe any novel phonetic, grammatical, or syntactic elements that reflect the specified cognitive and cultural characteristics.

2. Lexicon and Grammar (250-300 words):
   a) Present a sample vocabulary of 10-15 words that demonstrate the language's unique features.
   b) Explain the grammatical structures that reflect the given cognitive framework.
   c) Provide 2-3 example sentences with translations and grammatical explanations.
   d) Describe how the language handles concepts that might be challenging to express in Earth languages.

3. Writing System (150-200 words):
   a) Design a writing system that complements the language's cognitive and cultural basis.
   b) Explain how the writing system reflects or enhances the language's unique features.
   c) Provide a visual representation or detailed description of how a short phrase would be written.

4. Cognitive Impact Analysis (200-250 words):
   a) Analyze how this language might influence thought patterns and perception.
   b) Discuss potential cognitive advantages or challenges for speakers of this language.
   c) Explore how the language might shape problem-solving approaches or creativity.

5. Cultural Implications (200-250 words):
   a) Explain how the language reflects and reinforces the specified cultural worldview.
   b) Discuss how social interactions and relationships might be influenced by this language.
   c) Speculate on the types of literature, art, or cultural practices that might emerge from this linguistic framework.

6. Comparative Linguistics (150-200 words):
   a) Compare your constructed language to existing Earth languages or linguistic theories.
   b) Identify any similarities or striking differences with known language families.
   c) Discuss how this language challenges or extends current understanding in linguistics.

7. Practical Application (100-150 words):
   a) Propose a practical application or experiment to study the effects of this language on cognition or culture.
   b) Suggest how insights from this constructed language could be applied to fields such as AI, cognitive science, or intercultural communication.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and cultural anthropology. Be creative in your language design while maintaining internal consistency and plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of linguistics, cognitive science, and cultural anthropology.",
            "The constructed language clearly reflects the given cognitive framework and cultural aspect.",
            "The language design is creative, internally consistent, and plausible.",
            "The response includes all required sections with appropriate depth and detail.",
            "The analysis of cognitive impacts and cultural implications is insightful and well-reasoned.",
            "The comparative linguistics section demonstrates knowledge of existing languages and linguistic theories.",
            "The practical application suggestion is innovative and relevant.",
            "The response uses appropriate terminology and provides clear explanations for complex concepts.",
            "The total response falls within the specified word count range and is well-formatted."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
