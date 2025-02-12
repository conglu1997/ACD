import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "Time",
            "Justice",
            "Consciousness",
            "Infinity",
            "Freedom",
            "Truth",
            "Love",
            "Chaos"
        ]
        sensory_modalities = [
            "Visual",
            "Auditory",
            "Tactile",
            "Olfactory",
            "Gustatory",
            "Proprioceptive",
            "Thermoceptive",
            "Nociceptive"
        ]
        cognitive_principles = [
            "Embodied cognition",
            "Predictive processing",
            "Cognitive load theory",
            "Dual coding theory",
            "Connectionism",
            "Gestalt psychology",
            "Cognitive dissonance",
            "Metacognition"
        ]
        return {
            "1": {
                "concept": random.choice(abstract_concepts),
                "from_modality": random.choice(sensory_modalities),
                "to_modality": random.choice(sensory_modalities),
                "cognitive_principle": random.choice(cognitive_principles)
            },
            "2": {
                "concept": random.choice(abstract_concepts),
                "from_modality": random.choice(sensory_modalities),
                "to_modality": random.choice(sensory_modalities),
                "cognitive_principle": random.choice(cognitive_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an innovative language system based on cognitive synesthesia principles, incorporating the cognitive principle of {t['cognitive_principle']}. Then use this system to translate the abstract concept of {t['concept']} from the {t['from_modality']} sensory modality to the {t['to_modality']} sensory modality. Your response should include:

1. Synesthetic Language System Design (300-350 words):
   a) Explain how your language system incorporates cognitive synesthesia principles.
   b) Describe how you've integrated {t['cognitive_principle']} into your language design.
   c) Detail the key features of your language that enable cross-modal translations.
   d) Provide at least two examples of how your system represents sensory experiences.
   e) Discuss any novel insights about language and cognition revealed by your system.

2. Concept Translation (250-300 words):
   a) Describe how the concept of {t['concept']} is typically understood or expressed in the {t['from_modality']} modality.
   b) Explain your process for translating this concept to the {t['to_modality']} modality using your synesthetic language system.
   c) Provide a detailed description or representation of {t['concept']} in the {t['to_modality']} modality.
   d) Discuss any challenges encountered in this translation and how your system addressed them.

3. Cognitive Analysis (250-300 words):
   a) Analyze how your translation might affect the understanding or experience of {t['concept']}.
   b) Explain how {t['cognitive_principle']} influences the cross-modal translation in your system.
   c) Discuss potential cognitive implications of expressing abstract concepts through different sensory modalities.
   d) Propose a hypothesis about how this type of synesthetic language might impact human cognition if widely adopted.

4. Practical Applications (200-250 words):
   a) Suggest three potential real-world applications of your synesthetic language system.
   b) Describe how your system could be used to enhance communication or understanding in one specific field (e.g., education, therapy, art).
   c) Propose an experiment to test the effectiveness of your system in facilitating cross-modal thinking.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical implications of using a synesthetic language system.
   b) Address concerns about how this system might impact individuals with actual synesthesia.
   c) Identify at least two limitations of your system and propose ways to address them.
   d) Consider the potential long-term effects of widespread use of such a language system on human cognition and society.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and synesthesia. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative and push the boundaries of conventional thinking while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive synesthesia and {t['cognitive_principle']}.",
            "The synesthetic language system is innovative, well-designed, clearly explained, and incorporates the specified cognitive principle.",
            f"The translation of {t['concept']} from {t['from_modality']} to {t['to_modality']} modality is creative, detailed, and coherent.",
            "The cognitive analysis provides insightful implications of cross-modal concept expression.",
            "The practical applications suggested are innovative and well-reasoned.",
            "The ethical considerations and limitations are thoughtfully addressed.",
            "The response shows innovative thinking while maintaining scientific plausibility.",
            "The response adheres to the specified format, including headings and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
