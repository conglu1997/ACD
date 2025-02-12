import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = [
            ("Thermoception", "Temperature sensitivity"),
            ("Proprioception", "Body position sense"),
            ("Magnetoreception", "Magnetic field sensitivity"),
            ("Electroreception", "Electrical field sensitivity"),
            ("Echolocation", "Sound wave reflection sensing")
        ]
        linguistic_features = [
            "Tense system",
            "Evidentiality markers",
            "Honorifics",
            "Grammatical moods",
            "Aspectual distinctions"
        ]
        return {
            "1": {"modality": random.choice(sensory_modalities), "feature": random.choice(linguistic_features)},
            "2": {"modality": random.choice(sensory_modalities), "feature": random.choice(linguistic_features)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language based on the sensory modality of {t['modality'][0]} ({t['modality'][1]}), incorporating the linguistic feature of {t['feature']}. Then, create and interpret a message in this language. Your response should include:

1. Language Design (300-350 words):
   a) Explain how your language uses {t['modality'][0]} as its primary mode of communication.
   b) Describe the basic units of meaning in your language and how they are combined.
   c) Detail how you've incorporated {t['feature']} into the language structure.
   d) Discuss any unique challenges or advantages of using this sensory modality for language.

2. Cognitive and Neurological Basis (200-250 words):
   a) Explain how the brain might process and produce this language.
   b) Discuss how this language might influence or be influenced by cognitive processes.
   c) Speculate on any neuroplastic changes that might occur in fluent users of this language.

3. Message Creation and Interpretation (250-300 words):
   a) Create a short message (equivalent to 2-3 sentences) in your designed language. Describe the message using a combination of technical language and metaphorical descriptions to convey the sensory experience.
   b) Provide a detailed explanation of how this message is encoded and transmitted.
   c) Interpret the message, explaining how meaning is extracted from the sensory input.

4. Comparative Analysis (200-250 words):
   a) Compare your language to human spoken and signed languages.
   b) Discuss potential advantages or limitations of your language for different types of communication.
   c) Explore how this language might be adapted for use by humans or AI systems.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to the development and use of sensory languages.
   b) Explore possible societal impacts if such a language were to become widely adopted.
   c) Propose guidelines for responsible research and application of artificial sensory languages.

6. Comparative Reflection (100-150 words):
   Briefly compare your designed language to a hypothetical language based on a different sensory modality of your choice. Discuss how the choice of sensory modality influences the structure and capabilities of the language.

Ensure your response demonstrates a deep understanding of linguistics, sensory processing, and cognitive science. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your language design while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words.

Reminder: Adhere to the specified word count for each section as indicated above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified sensory modality and its potential for language.",
            f"The language design creatively incorporates the linguistic feature of {t['feature']}.",
            "The cognitive and neurological basis is explained plausibly and in detail.",
            "The created message and its interpretation are consistent with the described language system and effectively convey the sensory experience.",
            "The comparative analysis shows insightful understanding of human language systems.",
            "Ethical and societal implications are thoughtfully considered.",
            "The language design is both creative and plausible given the constraints of the sensory modality.",
            "The comparative reflection demonstrates an understanding of how different sensory modalities influence language structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
