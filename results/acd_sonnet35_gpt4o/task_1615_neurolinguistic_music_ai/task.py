import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            "Mandarin Chinese",
            "Arabic",
            "Quechua",
            "Finnish",
            "Xhosa"
        ]
        music_styles = [
            "Classical",
            "Jazz",
            "Electronic",
            "Folk",
            "Avant-garde"
        ]
        neurolinguistic_features = [
            "Tonal patterns",
            "Syntactic structures",
            "Phonemic inventories",
            "Prosodic features",
            "Semantic networks"
        ]
        return {
            "1": {
                "language": random.choice(languages),
                "music_style": random.choice(music_styles),
                "neurolinguistic_feature": random.choice(neurolinguistic_features)
            },
            "2": {
                "language": random.choice(languages),
                "music_style": random.choice(music_styles),
                "neurolinguistic_feature": random.choice(neurolinguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on neurolinguistic patterns of different languages, and analyze its implications for cognitive science and AI development. Your system should focus on the language {t['language']}, the music style {t['music_style']}, and the neurolinguistic feature of {t['neurolinguistic_feature']}. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for neurolinguistic music composition.
   b) Explain how your system integrates neurolinguistic analysis, music theory, and AI algorithms.
   c) Detail how the system adapts to the specified language, music style, and neurolinguistic feature.

2. Neurolinguistic-Musical Mapping (200-250 words):
   a) Explain how you map the chosen neurolinguistic feature to musical elements.
   b) Provide specific examples of how linguistic patterns in {t['language']} would be translated into musical patterns in the {t['music_style']} genre.
   c) Discuss any challenges in this mapping process and how you address them.

3. Composition Process (200-250 words):
   a) Describe step-by-step how your AI system would compose a piece of music.
   b) Explain how the system ensures the composition adheres to both linguistic patterns and musical conventions.
   c) Discuss how you balance creativity and adherence to the specified style and linguistic features.

4. Cognitive Science Implications (150-200 words):
   a) Analyze how your system's approach to music composition might inform our understanding of language processing in the human brain.
   b) Propose a hypothesis about the relationship between linguistic and musical cognition based on your system's design.

5. AI Development Insights (150-200 words):
   a) Discuss how the development of this system could contribute to advancements in AI, particularly in areas of creativity and cross-domain knowledge integration.
   b) Explore potential applications of your approach in other areas of AI research or development.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of AI systems that can mimic human cognitive processes in creative tasks.
   b) Propose two potential extensions or modifications to your system for future research.
   c) Suggest one experiment to validate the cognitive science hypothesis you proposed earlier.

Ensure your response demonstrates a deep understanding of neurolinguistics, music theory, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the language {t['language']}, the music style {t['music_style']}, and the neurolinguistic feature of {t['neurolinguistic_feature']}.",
            "The system architecture must demonstrate a clear integration of neurolinguistics, music theory, and AI.",
            "The neurolinguistic-musical mapping should be logical and well-explained.",
            "The composition process should be clearly described and should incorporate both linguistic and musical elements.",
            "The cognitive science implications should be thoughtful and well-reasoned.",
            "The AI development insights should be relevant and demonstrate an understanding of current AI challenges.",
            "The ethical considerations should be thorough and show an awareness of potential issues in AI creativity.",
            "The response should include all six required sections and adhere to the specified word counts.",
            "The proposed system should be innovative and demonstrate a deep understanding of all involved disciplines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
