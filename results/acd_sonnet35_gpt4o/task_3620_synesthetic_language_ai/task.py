import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_culture": "Japanese",
                "target_culture": "Maasai",
                "concept": "wabi-sabi (imperfect beauty)",
                "primary_modality": "visual",
                "secondary_modality": "auditory"
            },
            {
                "source_culture": "Inuit",
                "target_culture": "Brazilian",
                "concept": "sila (weather-wisdom balance)",
                "primary_modality": "tactile",
                "secondary_modality": "olfactory"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating and interpreting a synesthetic language that maps sensory experiences across different modalities, then use it to translate the concept of {t['concept']} from {t['source_culture']} culture to {t['target_culture']} culture. Your system should primarily use the {t['primary_modality']} modality, with {t['secondary_modality']} as a secondary modality.

Example sensory mappings:
- Visual to Auditory: Bright colors -> High-pitched sounds, Dark colors -> Low-pitched sounds
- Tactile to Olfactory: Rough textures -> Strong, spicy scents, Smooth textures -> Mild, sweet scents

Your response should include:

1. Synesthetic Language Design (300-350 words):
   a) Describe the key components of your AI system for creating and interpreting synesthetic language.
   b) Explain how it maps sensory experiences across {t['primary_modality']} and {t['secondary_modality']} modalities.
   c) Detail how the system incorporates cultural context in its language creation process.
   d) Provide examples of how basic concepts might be represented in this synesthetic language.

2. Cultural Context Analysis (200-250 words):
   a) Analyze the cultural significance of {t['concept']} in {t['source_culture']} culture.
   b) Discuss potential challenges in translating this concept to {t['target_culture']} culture.
   c) Explain how your system accounts for cultural nuances and differences.

3. Synesthetic Translation Process (250-300 words):
   a) Describe step-by-step how your AI system would translate {t['concept']} from {t['source_culture']} to {t['target_culture']} culture using the synesthetic language.
   b) Explain how the system ensures the translated concept maintains its core meaning while being culturally relevant to the target culture.
   c) Provide a detailed example of the synesthetic representation of the translated concept, describing both {t['primary_modality']} and {t['secondary_modality']} components.

4. Cross-Cultural Communication Application (200-250 words):
   a) Propose a practical application of your synesthetic language system in facilitating cross-cultural communication.
   b) Discuss potential benefits and challenges of using this system in real-world scenarios.
   c) Suggest how this system could be used to bridge cultural gaps or promote mutual understanding.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical implications of using AI-generated synesthetic languages for cross-cultural communication.
   b) Discuss any limitations of your approach and how they might be addressed.
   c) Propose guidelines for the responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility and cultural sensitivity. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as outlined above. Include the word count for each section in parentheses at the end of the section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the required format with clear headings and word counts for each section.",
            f"The synesthetic language design effectively maps {t['primary_modality']} and {t['secondary_modality']} modalities in an innovative and plausible way.",
            f"The cultural analysis of {t['concept']} is accurate and insightful for both {t['source_culture']} and {t['target_culture']} cultures.",
            f"A detailed example of the synesthetic representation of the translated {t['concept']} is provided, including both {t['primary_modality']} and {t['secondary_modality']} components.",
            "The proposed application for cross-cultural communication is practical and well-reasoned.",
            "Ethical considerations and limitations are thoughtfully addressed, with clear guidelines for responsible development and use.",
            "The response demonstrates a deep understanding of linguistics, cognitive science, cultural anthropology, and artificial intelligence throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
