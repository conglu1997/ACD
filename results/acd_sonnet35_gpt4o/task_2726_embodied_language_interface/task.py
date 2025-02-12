import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("English", "Mandarin Chinese"),
            ("Spanish", "Japanese"),
            ("Arabic", "Russian"),
            ("French", "Swahili")
        ]
        embodied_concepts = [
            "Spatial relations",
            "Emotional expressions",
            "Gestural communication",
            "Sensory metaphors"
        ]
        interface_types = [
            "Virtual reality",
            "Augmented reality",
            "Haptic feedback system",
            "Brain-computer interface"
        ]
        return {
            "1": {
                "language_pair": random.choice(language_pairs),
                "embodied_concept": random.choice(embodied_concepts),
                "interface_type": random.choice(interface_types)
            },
            "2": {
                "language_pair": random.choice(language_pairs),
                "embodied_concept": random.choice(embodied_concepts),
                "interface_type": random.choice(interface_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel human-computer interface based on principles of embodied cognition to facilitate language learning and cross-cultural communication. Your interface should focus on the language pair {t['language_pair'][0]} and {t['language_pair'][1]}, emphasizing the embodied concept of {t['embodied_concept']}, and utilizing {t['interface_type']} technology.

Your response should include the following sections:

1. Theoretical Framework (200-250 words)
2. Interface Design (250-300 words)
3. Learning Scenarios (200-250 words)
4. Cognitive and Linguistic Analysis (200-250 words)
5. Ethical Considerations and Limitations (150-200 words)

For each section, address the following key points:

1. Theoretical Framework:
   - Explain key principles of embodied cognition relevant to language learning
   - Apply these principles to the chosen language pair and embodied concept
   - Analyze challenges and opportunities in using {t['interface_type']} for embodied language learning

2. Interface Design:
   - Describe main components and functioning of your interface
   - Explain how it incorporates the chosen embodied concept
   - Detail how the interface uses {t['interface_type']} technology
   - Provide a high-level textual description of your interface design

3. Learning Scenarios:
   - Present two specific scenarios demonstrating user interaction
   - Explain how these scenarios enhance language acquisition and cross-cultural understanding
   - Compare your embodied approach to traditional language learning methods

4. Cognitive and Linguistic Analysis:
   - Analyze how your interface might influence cognitive processes in language learning
   - Discuss potential effects on neural plasticity and memory formation
   - Explain how your approach bridges linguistic and cultural gaps
   - Address potential cognitive or linguistic challenges

5. Ethical Considerations and Limitations:
   - Discuss ethical implications of using embodied cognition in language learning
   - Address issues related to cultural representation and appropriation
   - Explain limitations and areas for improvement
   - Propose guidelines for responsible development and use

Ensure your response demonstrates understanding of cognitive science, linguistics, and human-computer interaction. Use appropriate terminology and provide clear explanations. Be innovative while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs. Your total response should be between 1000-1250 words.

Example format for each section:

[Section Title]
1. [First paragraph]
2. [Second paragraph]
...
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of embodied cognition principles applied to language learning for {t['language_pair'][0]} and {t['language_pair'][1]}.",
            f"The interface design incorporates {t['embodied_concept']} and uses {t['interface_type']} technology innovatively.",
            "The learning scenarios show clear advantages over traditional language learning methods.",
            "The cognitive and linguistic analysis addresses effects on neural plasticity, memory formation, and cross-cultural understanding.",
            "Ethical considerations and limitations are addressed, including cultural representation issues.",
            "The response integrates concepts from cognitive science, linguistics, and human-computer interaction.",
            "The response follows the specified format with clear headings and numbered paragraphs.",
            "The total word count is between 1000-1250 words."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
