import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "source_language": "Mandarin Chinese",
                "target_language": "Spanish",
                "domain": "Business Negotiation",
                "concept": "Trust"
            },
            {
                "source_language": "Arabic",
                "target_language": "Japanese",
                "domain": "Environmental Diplomacy",
                "concept": "Sustainability"
            },
            {
                "source_language": "Russian",
                "target_language": "Swahili",
                "domain": "Cultural Exchange",
                "concept": "Harmony"
            },
            {
                "source_language": "Hindi",
                "target_language": "Portuguese",
                "domain": "Technology Innovation",
                "concept": "Progress"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing, interpreting, and generating metaphors across multiple languages and cultures. Then, apply your system to the following scenario:

Source Language: {t['source_language']}
Target Language: {t['target_language']}
Domain: {t['domain']}
Concept to Metaphorize: {t['concept']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system for cross-lingual metaphor processing.
   b) Explain how your system integrates linguistic, cultural, and cognitive models.
   c) Discuss any novel techniques or algorithms used in your design.
   d) Include a high-level diagram or pseudocode representing the system's workflow.

2. Metaphor Analysis and Interpretation (250-300 words):
   a) Explain how your system analyzes and interprets metaphors in the source language.
   b) Describe the methods used to capture cultural nuances and connotations.
   c) Discuss how your system handles ambiguity and context-dependence in metaphors.

3. Cross-Lingual Metaphor Generation (250-300 words):
   a) Describe the process of generating equivalent or similar metaphors in the target language.
   b) Explain how your system ensures cultural appropriateness and maintains the original meaning.
   c) Discuss any techniques used to enhance creativity in metaphor generation.

4. Cognitive Modeling of Figurative Language (200-250 words):
   a) Explain how your system models the cognitive processes involved in metaphor comprehension and production.
   b) Discuss how this cognitive model influences the system's analysis and generation capabilities.
   c) Describe any incorporation of embodied cognition or conceptual blending theories.

5. Scenario Application (250-300 words):
   a) Apply your system to the given scenario, providing step-by-step analysis.
   b) Generate a metaphor for the specified concept in the source language.
   c) Show how your system would analyze and interpret this metaphor.
   d) Demonstrate the generation of an equivalent metaphor in the target language.
   e) Explain any cultural adaptations made during the process.

6. Evaluation and Ethical Considerations (150-200 words):
   a) Propose methods to evaluate the effectiveness and cultural sensitivity of your system.
   b) Discuss potential biases or limitations in your approach.
   c) Address ethical concerns related to AI-generated figurative language in cross-cultural communication.

Ensure your response demonstrates a deep understanding of linguistics, cultural studies, cognitive science, and AI technologies. Be creative in your approach while maintaining scientific and ethical plausibility. Your total response should be between 1400-1700 words.

Format your response with clear headings for each section (e.g., '1. System Architecture', '2. Metaphor Analysis and Interpretation', etc.) and use subheadings (a, b, c, d, e) as outlined above. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of metaphor processing across languages and cultures.",
            "The AI system design integrates linguistic, cultural, and cognitive models effectively.",
            "The metaphor analysis and generation processes are well-explained and culturally sensitive.",
            "The application to the given scenario is detailed and demonstrates the system's capabilities.",
            "The generated metaphors in both source and target languages are creative and culturally appropriate.",
            "Ethical considerations and evaluation methods are thoroughly discussed.",
            "The response follows the specified format with clear headings and subheadings.",
            "The word count is within the specified range of 1400-1700 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
