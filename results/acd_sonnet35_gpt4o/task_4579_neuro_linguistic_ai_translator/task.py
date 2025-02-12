import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            'Broca\'s area',
            'Wernicke\'s area',
            'Angular gyrus',
            'Inferior frontal gyrus',
            'Superior temporal gyrus'
        ]
        alien_language_features = [
            'Temporal-based grammar',
            'Quantum superposition semantics',
            'Multi-dimensional phonemes',
            'Emotion-integrated syntax',
            'Non-linear logical structures'
        ]
        tasks = [
            {
                'brain_region': random.choice(brain_regions),
                'alien_language_feature': random.choice(alien_language_features)
            },
            {
                'brain_region': random.choice(brain_regions),
                'alien_language_feature': random.choice(alien_language_features)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical AI system that translates between human thoughts (as represented by neural activity patterns in {t['brain_region']}) and a hypothetical alien language with the feature of {t['alien_language_feature']}. Then, use your system to facilitate communication in a first contact scenario. Your response should include the following sections:

1. Neural-Linguistic Interface (300-350 words):
   a) Describe how your AI system interprets neural activity from {t['brain_region']}.
   b) Explain how the system maps these neural patterns to semantic concepts.
   c) Discuss any novel techniques or algorithms you incorporate for improved accuracy.
   d) Address how your system handles the variability in neural activity across individuals.

2. Alien Language Model (250-300 words):
   a) Design a model for the alien language, incorporating the feature of {t['alien_language_feature']}.
   b) Explain how this feature influences the language's structure and meaning.
   c) Describe how your AI system represents and processes this alien language.
   d) Discuss challenges in modeling a language with features unlike human languages.

3. Translation Mechanism (250-300 words):
   a) Explain how your system translates between neural activity and the alien language.
   b) Describe any intermediate representations or processes used in translation.
   c) Discuss how the system ensures accurate preservation of meaning across translations.
   d) Address how the system handles concepts that may not have direct equivalents.

4. First Contact Scenario (200-250 words):
   a) Describe a hypothetical first contact scenario where your system is used.
   b) Explain how your system facilitates initial communication and understanding.
   c) Discuss potential misunderstandings or challenges that could arise and how your system might address them.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of an AI system that can 'read' thoughts and translate alien languages.
   b) Explore the philosophical implications of this technology for our understanding of language, thought, and communication.
   c) Address potential risks or misuses of such a system and propose safeguards.

6. Future Developments and Applications (150-200 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Propose an innovative application of this technology beyond alien communication.
   c) Speculate on how this technology might influence human language and cognition in the long term.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neural activity in {t['brain_region']} and how it relates to language processing.",
            f"The alien language model creatively incorporates the feature of {t['alien_language_feature']} in a scientifically plausible way.",
            "The translation mechanism between neural activity and alien language is logically consistent and innovative.",
            "The first contact scenario effectively demonstrates the use of the AI system in a realistic and challenging situation.",
            "The response addresses ethical and philosophical implications thoughtfully and thoroughly.",
            "The proposed future developments and applications are creative and grounded in the capabilities of the designed system.",
            "The overall response shows a high level of interdisciplinary integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
