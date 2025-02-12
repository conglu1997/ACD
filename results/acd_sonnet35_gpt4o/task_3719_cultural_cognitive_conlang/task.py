import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_contexts = [
            "nomadic desert tribe",
            "advanced underwater civilization",
            "tree-dwelling forest community",
            "subterranean fungal symbiosis society",
            "plasma-based lifeforms in a gas giant"
        ]
        cognitive_constraints = [
            "limited short-term memory",
            "synesthesia-like sensory integration",
            "hive-mind collective consciousness",
            "non-linear time perception",
            "quantum entanglement-based cognition"
        ]
        complex_concepts = [
            "the beauty of impermanence",
            "the nature of consciousness",
            "the concept of infinity",
            "the balance between chaos and order",
            "the interconnectedness of all things"
        ]
        return {
            "1": {
                "cultural_context": random.choice(cultural_contexts),
                "cognitive_constraint": random.choice(cognitive_constraints),
                "complex_concept": random.choice(complex_concepts)
            },
            "2": {
                "cultural_context": random.choice(cultural_contexts),
                "cognitive_constraint": random.choice(cognitive_constraints),
                "complex_concept": random.choice(complex_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system (conlang or constructed language) for a {t['cultural_context']} with the cognitive constraint of {t['cognitive_constraint']}. Then, use this system to express the complex concept of {t['complex_concept']}. Your response should include the following sections:

1. Cultural and Cognitive Analysis (200-250 words):
   a) Describe the key characteristics of the given cultural context and how they might influence communication.
   b) Explain how the specified cognitive constraint would affect language processing and production.
   c) Discuss potential challenges and unique opportunities these factors present for designing a communication system.

2. Conlang Design (300-350 words):
   a) Outline the core features of your communication system, including its basic units (e.g., phonemes, graphemes, gestures) and how they combine.
   b) Explain how your system reflects the cultural context and accommodates the cognitive constraint.
   c) Describe the syntax and grammar of your conlang, providing examples of simple phrases or sentences.
   d) Discuss any unique or innovative aspects of your system that address specific cultural or cognitive needs.

3. Lexicon Development (200-250 words):
   a) Describe the process of creating words or symbols in your conlang.
   b) Provide a sample lexicon of at least 10 words or concepts that would be particularly important in the given cultural context.
   c) Explain how these words reflect cultural values, environmental factors, or cognitive processes.

4. Concept Translation (250-300 words):
   a) Translate the given complex concept into your conlang, providing the following:
      - Original concept in English
      - Translation in your conlang (using Latin script or clear notation)
      - Phonetic transcription (if applicable)
      - Literal back-translation to English
   b) Explain your translation process and any challenges you encountered.
   c) Discuss how your conlang's features allow for unique or nuanced expression of this concept.
   d) Analyze how this translation might differ from expressions of the same concept in other languages or cultures.

5. Communication System Analysis (200-250 words):
   a) Evaluate the strengths and limitations of your conlang in expressing complex ideas.
   b) Discuss how your system might evolve over time within the given cultural context.
   c) Propose a method for teaching this communication system to others, considering the cognitive constraint.

6. Linguistic and Cognitive Implications (150-200 words):
   a) Discuss what your conlang reveals about the relationship between language, culture, and cognition.
   b) Propose a hypothesis about how this communication system might influence thought patterns or worldviews.
   c) Suggest an experiment to test this hypothesis.

Ensure your response demonstrates creativity, cultural sensitivity, and a deep understanding of linguistics and cognitive science. Use appropriate terminology and provide clear explanations where necessary. Format your response with clear headings for each section, and make sure to address all points in each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design clearly reflects the cultural context of {t['cultural_context']} and accommodates the cognitive constraint of {t['cognitive_constraint']}.",
            "The conlang has a well-defined structure with clear explanations of its core features, syntax, and grammar.",
            "The sample lexicon is culturally relevant and well-explained.",
            f"The translation of '{t['complex_concept']}' into the conlang is provided with a thoughtful explanation of the process and challenges.",
            "The response demonstrates creativity, cultural sensitivity, and a deep understanding of linguistics and cognitive science.",
            "The analysis of the communication system and its implications is insightful and well-reasoned.",
            "The response addresses all required sections and adheres to the specified word counts and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
