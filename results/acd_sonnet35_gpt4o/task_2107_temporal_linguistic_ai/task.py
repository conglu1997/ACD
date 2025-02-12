import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        temporal_frameworks = [
            {
                "culture": "Linear (Western)",
                "time_concept": "Past, present, future as a line",
                "linguistic_feature": "Tense-based grammar"
            },
            {
                "culture": "Cyclic (Hindu)",
                "time_concept": "Repeating cycles of creation and destruction",
                "linguistic_feature": "Aspect-based verb forms"
            },
            {
                "culture": "Dreamtime (Aboriginal Australian)",
                "time_concept": "Past and present coexist in spiritual realm",
                "linguistic_feature": "Temporal distance markers"
            },
            {
                "culture": "Spiral (Mayan)",
                "time_concept": "Cyclical but progressive time",
                "linguistic_feature": "Complex calendar-based time references"
            }
        ]
        
        scientific_concepts = [
            "Entropy and the arrow of time",
            "Quantum superposition and temporal uncertainty",
            "Relativistic time dilation",
            "Chronobiology and circadian rhythms"
        ]
        
        alternative_approaches = [
            "Rule-based system",
            "Neural machine translation",
            "Symbolic AI",
            "Hybrid neuro-symbolic system"
        ]
        
        return {
            "1": {
                "framework": random.choice(temporal_frameworks),
                "concept": random.choice(scientific_concepts),
                "case_study": random.choice(["Ancient artifact dating", "Interstellar communication", "Geological time scales", "Biological aging processes"]),
                "alternative_approach": random.choice(alternative_approaches)
            },
            "2": {
                "framework": random.choice(temporal_frameworks),
                "concept": random.choice(scientific_concepts),
                "case_study": random.choice(["Ancient artifact dating", "Interstellar communication", "Geological time scales", "Biological aging processes"]),
                "alternative_approach": random.choice(alternative_approaches)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can understand and generate descriptions of temporal experiences based on the {t['framework']['culture']} framework, which conceptualizes time as {t['framework']['time_concept']} and uses {t['framework']['linguistic_feature']}. Then, use this system to translate and explain the scientific concept of {t['concept']} within this temporal-linguistic framework.

Your response should include the following sections, with the specified word counts:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for temporal-linguistic understanding and generation.
   b) Explain how it incorporates the given cultural framework's time concept.
   c) Detail how the system handles the specified linguistic feature for expressing time.
   d) Discuss any novel approaches or mechanisms in your design.
   e) Provide a small code snippet or pseudocode (30-50 lines) demonstrating a key aspect of your system's implementation.

2. Temporal-Linguistic Mapping (250-300 words):
   a) Explain how your system maps between the given cultural time concept and more familiar temporal frameworks.
   b) Provide examples of how common temporal expressions would be understood or generated in this framework.
   c) Discuss challenges in representing this temporal framework computationally and how you address them.

3. Scientific Concept Translation (300-350 words):
   a) Briefly explain the given scientific concept in standard terms (50-75 words).
   b) Describe how your AI system would translate this concept into the given temporal-linguistic framework.
   c) Provide a sample output of your system explaining the concept in this framework (100-150 words).
   d) Analyze how this translation process affects the understanding or presentation of the scientific concept.

4. Case Study: {t['case_study']} (200-250 words):
   a) Apply your AI system to the given case study.
   b) Explain how the system would handle temporal aspects of this scenario within the given framework.
   c) Discuss any insights or challenges that arise from this application.

5. Cross-Cultural Temporal Reasoning (200-250 words):
   a) Discuss how your system might handle transitions between different temporal-linguistic frameworks.
   b) Explore potential insights or challenges that arise when expressing scientific concepts across diverse temporal frameworks.
   c) Propose an experiment to test the system's effectiveness in cross-cultural temporal communication.

6. Limitations and Comparisons (200-250 words):
   a) Discuss potential limitations or edge cases of your proposed AI system.
   b) Compare your system to a {t['alternative_approach']} approach for this task.
   c) Justify your design choices in light of this comparison.

7. Implications and Ethics (200-250 words):
   a) Discuss the potential implications of this technology for cross-cultural communication and scientific education.
   b) Explore ethical considerations in developing AI systems that operate across diverse cultural frameworks.
   c) Suggest guidelines for responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, the specified temporal framework, and the given scientific concept. Be creative and original in your approach while maintaining scientific plausibility. Merely rephrasing the provided information is insufficient; novel solutions and insights are required. Use clear headings for each section of your response. Your total response should be between 1650-2000 words.

Evaluation Criteria:
1. Comprehensive understanding of the given temporal-linguistic framework and scientific concept.
2. Effective incorporation of the specified cultural time concept and linguistic feature in the AI system design.
3. Creativity, coherence, and fidelity in the scientific concept translation.
4. Insightful application of the AI system to the given case study.
5. Thoughtful discussion of cross-cultural temporal reasoning and ethical implications.
6. Critical analysis of system limitations and comparison with the alternative approach.
7. Quality and relevance of the provided code snippet or pseudocode.
8. Overall structure, creativity, and scientific plausibility of the response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the given temporal-linguistic framework and scientific concept.",
            "The AI system design effectively incorporates the specified cultural time concept and linguistic feature.",
            "The scientific concept translation is creative, coherent, and faithful to both the original concept and the given temporal framework.",
            "The case study application is insightful and demonstrates the AI system's capabilities effectively.",
            "The discussion of cross-cultural temporal reasoning is insightful and considers multiple perspectives.",
            "The response critically analyzes system limitations and provides a meaningful comparison with the alternative approach.",
            "The provided code snippet or pseudocode is relevant and demonstrates a key aspect of the system's implementation.",
            "The response addresses ethical implications and provides thoughtful guidelines for responsible development.",
            "The overall response is well-structured, creative, original, and scientifically plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
